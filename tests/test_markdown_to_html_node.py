"""Testing module for markdown_to_html_node module"""

import unittest

from src.markdown_to_html_node import markdown_to_html_node


class TestMarkdownToHTMLNode(unittest.TestCase):
    """Will contain all cases from testing the module"""

    def test_paragraphs(self):
        md = """
    This is **bolded** paragraph text in a p tag here

    This is another paragraph with _italic_ text and `code` here

    """

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

    def test_codeblock(self):
        md = """
    ```
    This is text that _should_ remain
    the **same** even with inline stuff
    ```
    """

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            ("<div><pre><code>This is text that _should_ remain\n"
             "the **same** even with inline stuff\n</code></pre></div>"),
        )

    def test_ordered_list(self):
        """Will test case of ordered list"""

        md = """
        1. This is ordered list first element
        2. This is ordered list second element
        3. This is ordered list third element
        """
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            ("<div><ol><li>This is ordered list first element</li>"
             "<li>This is ordered list second element</li>"
             "<li>This is ordered list third element</li></ol></div>")
        )

    def test_unordered_list(self):
        """Will test case of unordered list"""

        md = """
           - This is unordered list first element
           - This is unordered list second element
           - This is unordered list third element
        """

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            ("<div><ul><li>This is unordered list first element</li>"
             "<li>This is unordered list second element</li>"
             "<li>This is unordered list third element</li></ul></div>"
             )
        )

    def test_blockquote(self):
        """ Will test case of blockquote"""

        md = """
            > This is a text within a blockquote
            > and another line
            > and the last one
        """

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            ("<div><blockquote>This is a text within a blockquote<br/>"
             "and another line<br/>"
             "and the last one<br/></blockquote></div>"
             )
        )

    # TODO create tests for other block types
