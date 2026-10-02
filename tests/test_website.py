import shutil
import subprocess
import unittest
from helpers import ROOT, html_files, parse

NAV_PAGES = ["index.html", "about.html", "projects.html", "contact.html"]


class WebsiteTests(unittest.TestCase):
    def test_navigation_on_every_page(self):
        for path in html_files():
            with self.subTest(page=path.name):
                links = " ".join(parse(path).links)
                for target in NAV_PAGES:
                    self.assertIn(target, links)

    def test_viewport_meta_for_responsive_layout(self):
        for path in html_files():
            with self.subTest(page=path.name):
                self.assertIn('name="viewport"', path.read_text(encoding="utf-8"))

    def test_contact_form_fields(self):
        html = (ROOT / "contact.html").read_text(encoding="utf-8")
        for field in ('id="name"', 'id="email"', 'id="message"', 'id="contact-form"'):
            self.assertIn(field, html)

    def test_css_is_balanced_and_responsive(self):
        css = (ROOT / "css" / "style.css").read_text(encoding="utf-8")
        self.assertEqual(css.count("{"), css.count("}"))
        self.assertIn("@media", css)

    def test_homepage_content(self):
        page = parse(ROOT / "index.html")
        self.assertIn("Home", page.title)

    @unittest.skipUnless(shutil.which("node"), "node not installed")
    def test_javascript_syntax(self):
        for js in sorted((ROOT / "js").glob("*.js")):
            with self.subTest(script=js.name):
                result = subprocess.run(["node", "--check", str(js)], capture_output=True, text=True)
                self.assertEqual(result.returncode, 0, result.stderr)


if __name__ == "__main__":
    unittest.main()
