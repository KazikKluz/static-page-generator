from textnode import TextNode, TextType


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    if old_nodes.text_type != "text":
        return [old_nodes]

    split_text = old_nodes.text.split(delimiter)

    if len(split_text) % 2 == 0:
        raise ValueError("Invalid Markdown syntax")

    split_nodes = []

    for i in range(0, len(split_text)):
        if i % 2 == 0:
            node_type = TextType.TEXT
        else:
            node_type = text_type
        split_nodes.append(TextNode(split_text[i], node_type))

    return split_nodes
