from split_delimiter import split_nodes_delimiter, split_nodes_image, split_nodes_link
from textnode import TextNode, TextType


def text_to_nodes(text):
    node = TextNode(text, TextType.TEXT)

    more_nodes = images_and_links([node])

    even_more_nodes = delimiters(more_nodes)

    return even_more_nodes


def delimiters(nodes):
    args = [("**", TextType.BOLD), ("_", TextType.ITALIC), ("`", TextType.CODE)]

    for arg in args:
        temp = []
        for node in nodes:
            if node.text_type == "text":
                more = split_nodes_delimiter(node, arg[0], arg[1])
                temp.extend(more)

            else:
                temp.append(node)
        nodes = temp.copy()
    return nodes


def images_and_links(nodes):
    functions = [split_nodes_image, split_nodes_link]

    for func in functions:
        temp = []
        for node in nodes:
            if node.text_type == "text":
                more = func(node)
                if isinstance(more, list):
                    temp.extend(more)
                else:
                    temp.append(more)
            else:
                temp.append(node)
        nodes = temp.copy()

    return nodes
