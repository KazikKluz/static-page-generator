import unittest

from text_to_nodes import text_to_nodes
from textnode import TextNode, TextType


class TestTextToNodes(unittest.TestCase):
    def test_basic(self):
        a_text = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"

        result = text_to_nodes(a_text)
        self.assertListEqual(
            [
                TextNode("This is ", TextType.TEXT),
                TextNode("text", TextType.BOLD),
                TextNode(" with an ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
                TextNode(" word and a ", TextType.TEXT),
                TextNode("code block", TextType.CODE),
                TextNode(" and an ", TextType.TEXT),
                TextNode(
                    "obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"
                ),
                TextNode(" and a ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://boot.dev"),
            ],
            result,
        )

    def test_just_text(self):
        a_text = "This is text with an italic word and a code block and an and a."

        result = text_to_nodes(a_text)
        self.assertListEqual(
            [
                TextNode(
                    "This is text with an italic word and a code block and an and a.",
                    TextType.TEXT,
                ),
            ],
            result,
        )

    def test_just_links(self):
        a_text = (
            "[obi wan image](https://i.imgur.com/fJRm4Vk.jpeg)[link](https://boot.dev)"
        )

        result = text_to_nodes(a_text)
        self.assertListEqual(
            [
                TextNode(
                    "obi wan image", TextType.LINK, "https://i.imgur.com/fJRm4Vk.jpeg"
                ),
                TextNode("link", TextType.LINK, "https://boot.dev"),
            ],
            result,
        )

    def test_just_images(self):
        a_text = "![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg)![link](https://boot.dev)"

        result = text_to_nodes(a_text)
        self.assertListEqual(
            [
                TextNode(
                    "obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"
                ),
                TextNode("link", TextType.IMAGE, "https://boot.dev"),
            ],
            result,
        )

    def test_just_bold(self):
        a_text = "**This is bold text**"

        result = text_to_nodes(a_text)
        self.assertListEqual(
            [
                TextNode("This is bold text", TextType.BOLD),
            ],
            result,
        )

    def test_just_code(self):
        a_text = "`This is code`"

        result = text_to_nodes(a_text)
        self.assertListEqual(
            [
                TextNode("This is code", TextType.CODE),
            ],
            result,
        )

    def test_just_italic(self):
        a_text = "_This is italic text_"

        result = text_to_nodes(a_text)
        self.assertListEqual(
            [
                TextNode("This is italic text", TextType.ITALIC),
            ],
            result,
        )

    def test_just_x(self):
        a_text = "_This is italic text_"

        result = text_to_nodes(a_text)
        self.assertListEqual(
            [
                TextNode("This is italic text", TextType.ITALIC),
            ],
            result,
        )
