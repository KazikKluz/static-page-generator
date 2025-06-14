from split_delimiter import split_nodes_delimiter
from textnode import TextNode, TextType


def main():
    node = TextNode("This is some anchor text", TextType.LINK, "https://www.boot.dev")

    node2 = TextNode("This is **bold** text", TextType.TEXT)

    nodes = split_nodes_delimiter(node2, "**", TextType.BOLD)

    print(nodes)


main()
