"""Small offline regression check for the source-list parser."""
import unittest
from download_exams import Links

class DownloadListingTests(unittest.TestCase):
    def test_pdf_labels_and_navigation(self):
        parser = Links()
        parser.feed('<a href="/paper.pdf"><b>Higher</b> (EV)</a><a href="/2025">year</a>')
        self.assertEqual(parser.links, [['/paper.pdf', 'Higher (EV)']])

    def test_empty_listing(self):
        parser = Links()
        parser.feed('<p>No documents available</p>')
        self.assertEqual(parser.links, [])

if __name__ == '__main__':
    unittest.main()
