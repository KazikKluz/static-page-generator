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

    # TODO create tests for other block types
