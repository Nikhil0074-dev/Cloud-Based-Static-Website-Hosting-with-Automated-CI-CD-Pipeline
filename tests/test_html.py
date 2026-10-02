import unittest
from helpers import html_files, parse


class HtmlTests(unittest.TestCase):
    def test_pages_exist(self):
        names = {p.name for p in html_files()}
        for expected in ("index.html", "about.html", "projects.html", "contact.html", "404.html", "dashboard.html"):
            self.assertIn(expected, names)

    def test_each_page_is_well_formed(self):
        for path in html_files():
            with self.subTest(page=path.name):
                page = parse(path)
                self.assertTrue(page.doctype, "missing <!DOCTYPE html>")
                self.assertTrue(page.lang, "missing lang attribute on <html>")
                self.assertTrue(page.title.strip(), "missing <title>")
                for tag in ("head", "body", "main", "header", "footer", "nav"):
                    self.assertIn(tag, page.tags, "missing <%s>" % tag)
                self.assertEqual(page.errors, [])

    def test_ids_are_unique(self):
        for path in html_files():
            with self.subTest(page=path.name):
                ids = parse(path).ids
                self.assertEqual(len(ids), len(set(ids)), "duplicate ids: %s" % ids)


if __name__ == "__main__":
    unittest.main()
