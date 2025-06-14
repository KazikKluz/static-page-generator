import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode

test_prop1 = {
    "href": "https://www.google.com",
    "target": "_blank",
}

test_prop2 = {
    "href": "https://www.facebook.com",
    "target": "_blank",
}


class TestHTMLNode(unittest.TestCase):
    def test_prop_eq(self):
        props_html = ' href="https://www.google.com" target="_blank"'
        node = HTMLNode(tag="H1", props=test_prop1)
        self.assertEqual(props_html, node.props_to_html())

    def test_prop_not_eq(self):
        props_html = ' href="https://www.facebook.com" target="_blank"'
        node = HTMLNode(tag="H1", props=test_prop1)
        self.assertNotEqual(props_html, node.props_to_html())

    def test_prop_nodes_eq(self):
        node = HTMLNode(tag="H1", props=test_prop1)
        node2 = HTMLNode(tag="H5", props=test_prop1)
        self.assertEqual(node.props_to_html(), node2.props_to_html())


class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, World!")
        self.assertEqual(node.to_html(), "<p>Hello, World!</p>")


class TestParentNode(unittest.TestCase):
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grand_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(), "<div><span><b>grandchild</b></span></div>"
        )

    def test_to_html_mutliple_children(self):
        child_node1 = LeafNode("span", "brother")
        child_node2 = LeafNode("p", "sister")
        parent_node = ParentNode("div", [child_node1, child_node2])
        self.assertEqual(
            parent_node.to_html(), "<div><span>brother</span><p>sister</p></div>"
        )

    def test_no_children(self):
        parent_node = ParentNode("div", None)
        with self.assertRaises(ValueError):
            parent_node.to_html()

    def test_no_children2(self):
        child_node1 = LeafNode("span", "brother")
        parent_node = ParentNode(None, [child_node1])
        with self.assertRaises(ValueError):
            parent_node.to_html()

    def test_to_html_with_grand_grandchildren2(self):
        grandgrandchild_node = LeafNode("p", "grandgrandchild")
        grandchild_node = ParentNode("b", [grandgrandchild_node])
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b><p>grandgrandchild</p></b></span></div>",
        )
