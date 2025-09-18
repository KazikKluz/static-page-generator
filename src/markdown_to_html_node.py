"""converts a full markdown document into a single parent HTMLNode"""

from src.block_types import block_to_block_type
from src.htmlnode import LeafNode, ParentNode
from src.split_blocks import markdown_to_blocks
from src.text_to_nodes import text_to_nodes
from src.textnode import text_node_to_html_node


def markdown_to_html_node(doc):
    """Takes a chunk of Markdown and
    turns it into an HTML block
    """

    blocks = markdown_to_blocks(doc)

    nodes = []

    for block in blocks:
        block_type = block_to_block_type(block)

        match block_type.value:
            case "code":
                clean_content = process_code_block(block)
                leaf = LeafNode(None, clean_content)
                inner = ParentNode(block_type.value, [leaf])
                outer = ParentNode("pre", [inner])
                nodes.append(outer)

            case "ol" | "ul":
                children = process_list(block)
                node = ParentNode(block_type.value, children)
                nodes.append(node)

            case "p":
                children = text_to_children(block)
                node = ParentNode(block_type.value, children)
                nodes.append(node)

            case "blockquote":
                content = process_blockquote(block)
                leaf = LeafNode("br", "")

                print(f"leaf: {leaf.to_html()}")
                node = ParentNode(block_type.value, content)
                nodes.append(node)

    parent = ParentNode("div", nodes)

    return parent


def process_blockquote(text):
    """It takes a Markdown blockquote
    and converts it into HTML blockquote"""
    splited_text = text.split("\n")
    children = []

    for item in splited_text:
        new_item = item.strip().split(" ", 1)[1]
        children.append(LeafNode(None, new_item))
        children.append(LeafNode("br", ""))

    return children


def process_list(text):
    """It takes a Markdown list 
    and convert it into html list elements"""

    splited_text = text.split("\n")
    children = []

    for item in splited_text:
        # before passing it to function get rid of leading bullet point digit or dot
        new_item = text_to_children(item.strip().split(" ", 1)[1])
        leaf = ParentNode("li", new_item)
        children.append(leaf)

    return children


def process_code_block(text):
    """It takes markdown text
        and remove all leading and trailing
        indentations and new lines
    """
    stripped_block = text.strip("`").strip("\n")
    lines = stripped_block.splitlines()
    non_empty_lines = [line for line in lines if line.strip()]
    if non_empty_lines:
        indent = min(len(line) - len(line.lstrip())
                     for line in non_empty_lines)
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
