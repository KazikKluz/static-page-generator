"""converts a full markdown document into a single parent HTMLNode"""

from block_types import block_to_block_type
from htmlnode import LeafNode, ParentNode
from split_blocks import markdown_to_blocks
from text_to_nodes import text_to_nodes
from textnode import text_node_to_html_node


def markdown_to_html_node(doc):
    """Takes a chunk of Markdown and
    turns it into an HTML block
    """

    blocks = markdown_to_blocks(doc)

    nodes = []

    for block in blocks:
        block_type = block_to_block_type(block)

        if block_type.value == "code":
            clean_content = process_code_block(block)
            leaf = LeafNode(None, clean_content)
            inner = ParentNode(block_type.value, [leaf])
            outer = ParentNode("pre", [inner])

            nodes.append(outer)
        else:
            children = text_to_children(block)

            node = ParentNode(block_type.value, children)

            nodes.append(node)

    parent = ParentNode("div", nodes)

    return parent


def process_code_block(text):
    stripped_block = text.strip("`").strip("\n")
    lines = stripped_block.splitlines()
    non_empty_lines = [line for line in lines if line.strip()]
    if non_empty_lines:
        indent = min(len(line) - len(line.lstrip()) for line in non_empty_lines)
        lines = [line[indent:] if line.strip() else line for line in lines]
    clean_content = "\n".join(lines).rstrip() + "\n"

    return clean_content


def text_to_children(text):
    """It takes a string of text and returns a list of
    HTMLNodes that represent the inline markdown
    using previously created functions
    (TextNode -> HTMLNode)
    """
    htmlnode_list = []

    inline_text_list = text_to_nodes(text)

    for item in inline_text_list:
        html_node = text_node_to_html_node(item)
        htmlnode_list.append(html_node)

    return htmlnode_list
