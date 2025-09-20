""" Testing module for extract_title"""

import unittest

from src.extract_title import extract_title


class TestExtractTitle(unittest.TestCase):
    """Group of Tests for extract_title function"""

    def test_get_h1(self):
        """Will test case where there is a h1"""

        md = '''
        # This is a main title

        ## And this is not
        '''

        title = extract_title(md)
        self.assertEqual(title, "This is a main title")

    def test_get_h1_reversed(self):
        """Will test case where h1 is not first block"""

        md = '''
        ## This is a main title

        # And this is not
        '''

        title = extract_title(md)
        self.assertEqual(title, "And this is not")

    def test_no_h1(self):
        """Will test case where h1 is not present"""

        md = '''
        p This is a main title

        > And this is not
        '''

        with self.assertRaises(ValueError):
            extract_title(md)
