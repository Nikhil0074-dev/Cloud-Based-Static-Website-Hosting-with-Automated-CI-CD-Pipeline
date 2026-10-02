"""Shared helpers for the website tests (standard library only)."""
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent / "website"
VOID = {"meta", "link", "img", "br", "hr", "input", "source", "area", "base", "col", "embed", "wbr"}


def html_files():
    return sorted(ROOT.glob("*.html"))


class Page(HTMLParser):
    """Collects structure, links and errors from one HTML document."""

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.stack, self.errors = [], []
        self.links, self.assets, self.ids = [], [], []
        self.title, self._in_title = "", False
        self.doctype = False
        self.lang = None
        self.tags = set()

    def handle_decl(self, decl):
        if decl.lower().startswith("doctype html"):
            self.doctype = True

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        self.tags.add(tag)
        if tag == "html":
            self.lang = a.get("lang")
        if tag == "title":
            self._in_title = True
        if "id" in a:
            self.ids.append(a["id"])
        if tag == "a" and a.get("href"):
            self.links.append(a["href"])
        if tag in ("img", "script") and a.get("src"):
            self.assets.append(a["src"])
        if tag == "link" and a.get("href"):
            self.assets.append(a["href"])
        if tag == "img" and "alt" not in a:
            self.errors.append("<img> without alt attribute: %s" % a.get("src"))
        if tag not in VOID:
            self.stack.append(tag)

    def handle_endtag(self, tag):
        if tag == "title":
            self._in_title = False
        if tag in VOID:
            return
        if not self.stack or self.stack[-1] != tag:
            self.errors.append("Unexpected </%s>; open tags: %s" % (tag, self.stack))
            if tag in self.stack:
                while self.stack and self.stack.pop() != tag:
                    pass
        else:
            self.stack.pop()

    def handle_data(self, data):
        if self._in_title:
            self.title += data

    def close(self):
        super().close()
        if self.stack:
            self.errors.append("Unclosed tags: %s" % self.stack)


def parse(path):
    p = Page()
    p.feed(Path(path).read_text(encoding="utf-8"))
    p.close()
    return p
