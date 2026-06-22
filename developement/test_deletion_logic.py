import os
import sys
import unittest

# Ensure workspace root is in path
WORKSPACE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, WORKSPACE_DIR)

from web_app import BibleMateApp

class TestDeletionLogic(unittest.TestCase):
    def setUp(self):
        self.app = BibleMateApp()

    def test_protected_paths(self):
        protected_paths = [
            '.',
            '',
            'biblemate',
            'export',
            'export/md',
            'export/docx',
            'images',
            'images/readme.md',
            'images/readme',
            'biblemate/README.md',
            'export/README.md',
            'export/md/README.md',
            'export/docx/README.md',
            'images/README.md',
            'docs',
            'docs/help.md',
            'docs/subfolder/doc.txt',
            '../outside_file.txt',
            '/absolute/path/file.txt'
        ]
        for path in protected_paths:
            with self.subTest(path=path):
                self.assertFalse(self.app.is_deletable(path), f"Path '{path}' should NOT be deletable")

    def test_allowed_paths(self):
        allowed_paths = [
            'biblemate/2026-06-21-22-26-14_john_3_16_prayer.md',
            'biblemate/subfolder/file.md',
            'export/md/hope_study.md',
            'export/docx/love_analysis.docx',
            'images/2026-06-21-20-49-20_painting.png',
            'images/custom_subfolder/painting.jpg'
        ]
        for path in allowed_paths:
            with self.subTest(path=path):
                self.assertTrue(self.app.is_deletable(path), f"Path '{path}' should be deletable")

if __name__ == '__main__':
    unittest.main()
