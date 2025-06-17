import unittest

from split_delimiter import split_nodes_delimiter, split_nodes_image
from textnode import TextNode, TextType


class TestSplitDelimiter(unittest.TestCase):
    def test_basic(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter(node, "`", TextType.CODE)
        self.assertEqual(
            new_nodes,
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("code block", TextType.CODE),
                TextNode(" word", TextType.TEXT),
            ],
        )

    def test_double_bold(self):
        node = TextNode(
            "This is text with a **bold** word and **another bold** words.",
            TextType.TEXT,
        )
        new_nodes = split_nodes_delimiter(node, "**", TextType.BOLD)
        self.assertEqual(
            new_nodes,
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("bold", TextType.BOLD),
                TextNode(" word and ", TextType.TEXT),
                TextNode("another bold", TextType.BOLD),
                TextNode(" words.", TextType.TEXT),
            ],
        )

    def test_triple_italic(self):
        node = TextNode(
            "This is text with _italic_ word, then i add more _italic words_, and also _this part_ will be italic.",
            TextType.TEXT,
        )
        new_nodes = split_nodes_delimiter(node, "_", TextType.ITALIC)

        self.assertEqual(
            new_nodes,
            [
                TextNode("This is text with ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
                TextNode(" word, then i add more ", TextType.TEXT),
                TextNode("italic words", TextType.ITALIC),
                TextNode(", and also ", TextType.TEXT),
                TextNode("this part", TextType.ITALIC),
                TextNode(" will be italic.", TextType.TEXT),
            ],
        )

    def test_exception(self):
        node = TextNode(
            "This is text with _italic_ word, then i add more italic words_, and also _this part_ will be italic.",
            TextType.TEXT,
        )
        with self.assertRaises(ValueError):
            new_nodes = split_nodes_delimiter(node, "_", TextType.ITALIC)

    def test_split_images_even(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png) image.",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image(node)
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
                TextNode(" image.", TextType.TEXT),
            ],
            new_nodes,
        )

    def test_split_images_uneven(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image(node)
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )

    def test_split_images_no_fron_string(self):
        node = TextNode(
            "![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image(node)
        self.assertListEqual(
            [
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )

    def test_split_images_just_images(self):
        node = TextNode(
            "![image](https://i.imgur.com/zjjcJKZ.png)![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image(node)
        self.assertListEqual(
            [
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(
                    "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )
