import unittest
from urllib.parse import urlparse
from helpers import ROOT, html_files, parse


def resolve(page_path, ref):
    """Map a link/asset reference to a file under website/, or None if external."""
    u = urlparse(ref)
    if u.scheme in ("http", "https", "mailto", "tel", "data") or u.netloc:
        return None
    if not u.path:
        return page_path  # pure '#fragment'
    if u.path.startswith("/"):
        return ROOT / u.path.lstrip("/")
    return (page_path.parent / u.path).resolve()


class LinkTests(unittest.TestCase):
    def test_internal_links_and_assets_exist(self):
        for path in html_files():
            page = parse(path)
            for ref in page.links + page.assets:
                with self.subTest(page=path.name, ref=ref):
                    target = resolve(path, ref)
                    if target is not None:
                        self.assertTrue(target.exists(), "broken reference: %s" % ref)

    def test_fragment_targets_exist(self):
        for path in html_files():
            page = parse(path)
            for ref in page.links:
                u = urlparse(ref)
                if u.fragment and not u.path:
                    with self.subTest(page=path.name, ref=ref):
                        self.assertIn(u.fragment, page.ids)


if __name__ == "__main__":
    unittest.main()
