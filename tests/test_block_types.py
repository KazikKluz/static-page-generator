"""The module contains testing function for
different types of HTML blocks
"""

import unittest

from src.block_types import BlockType, block_to_block_type


class TestingBlockTypes(unittest.TestCase):
    """Class for testing block types"""

    def test_heading_1(self):
        """Simple HTML Header 1 testing"""
        block = "# This is a heading 1"
        self.assertEqual(block_to_block_type(block), BlockType.H1)

    def test_h1(self):
        """Checks non quality between H1 and H2"""
        self.assertNotEqual(block_to_block_type("## Hello "), BlockType.H1)

    def test_h2(self):
        self.assertEqual(block_to_block_type("## Hello "), BlockType.H2)

    def test_h3(self):
        self.assertEqual(block_to_block_type("### Hello "), BlockType.H3)

    def test_h4(self):
        self.assertEqual(block_to_block_type("#### Hello "), BlockType.H4)

    def test_h5(self):
        self.assertEqual(block_to_block_type("##### Hello "), BlockType.H5)

    def test_heading_6(self):
        block = "###### This is a heading 6"
        self.assertEqual(block_to_block_type(block), BlockType.H6)

    def test_h6(self):
        self.assertNotEqual("## Hello ", BlockType.H6)

    def test_code(self):
        block = "``` This is some code ```"
        self.assertEqual(block_to_block_type(block), BlockType.CODE)

    def test_not_code(self):
        block = "``` This is not code. So its a paragraph"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

    def test_quote(self):
        block = "> This is quote"
        self.assertEqual(block_to_block_type(block), BlockType.QUOTE)

    def test_ulist(self):
        block = "- This is first unordered list item.\n- This is second one"
        self.assertEqual(block_to_block_type(block), BlockType.ULIST)
