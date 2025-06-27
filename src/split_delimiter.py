from textnode import TextNode, TextType
from utils import extract_markdown_images, extract_markdown_links


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    if old_nodes.text_type != "text":
        return [old_nodes]

    split_text = old_nodes.text.split(delimiter)

    if len(split_text) % 2 == 0:
        raise ValueError("Invalid Markdown syntax")

    split_nodes = []

    for i in range(0, len(split_text)):
        if len(split_text[i]) == 0:
            continue
        if i % 2 == 0:
            node_type = TextType.TEXT
        else:
            node_type = text_type

        split_nodes.append(TextNode(split_text[i], node_type))

    return split_nodes


def split_nodes_image(old_nodes):
    matches = extract_markdown_images(old_nodes.text)

    if len(matches) == 0:
        return old_nodes

    extracted_nodes = []
    text_to_split = old_nodes.text

    while len(matches) > 0:
        delimiter = matches.pop(0)
        sections = text_to_split.split(f"![{delimiter[0]}]({delimiter[1]})", 1)

        if len(sections[0]) > 0:
            first = TextNode(sections[0], TextType.TEXT)
            extracted_nodes.append(first)
        second = TextNode(delimiter[0], TextType.IMAGE, delimiter[1])
        extracted_nodes.append(second)

        matches = extract_markdown_images(sections[1])
        text_to_split = sections[1]

    if len(text_to_split) > 0:
        extracted_nodes.append(TextNode(text_to_split, TextType.TEXT))

    return extracted_nodes


def split_nodes_link(old_nodes):
    matches = extract_markdown_links(old_nodes.text)

    if len(matches) == 0:
        return old_nodes

    extracted_nodes = []
    text_to_split = old_nodes.text

    while len(matches) > 0:
        delimiter = matches.pop(0)
        sections = text_to_split.split(f"[{delimiter[0]}]({delimiter[1]})", 1)

        if len(sections[0]) > 0:
            first = TextNode(sections[0], TextType.TEXT)
            extracted_nodes.append(first)
        second = TextNode(delimiter[0], TextType.LINK, delimiter[1])
        extracted_nodes.append(second)

        matches = extract_markdown_links(sections[1])
        text_to_split = sections[1]

    if len(text_to_split) > 0:
        extracted_nodes.append(TextNode(text_to_split, TextType.TEXT))

    return extracted_nodes
