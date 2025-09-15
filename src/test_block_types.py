"""The module contains testing function for
different types of HTML blocks
"""

import unittest

from block_types import BlockType, block_to_block_type


class TestingBlockTypes(unittest.TestCase):
    """Class for testing block types"""

    def test_heading_1(self):
        block = "# This is a heading 1"
        self.assertEqual(block_to_block_type(block), BlockType.H1)

    def test_heading_6(self):
        block = "###### This is a heading 6"
        self.assertEqual(block_to_block_type(block), BlockType.H6)

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
