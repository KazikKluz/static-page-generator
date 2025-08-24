"""converts a full markdown document into a single parent HTMLNode"""

from block_types import block_to_block_type
from split_blocks import markdown_to_blocks


def markdown_to_html_node(doc):
    """Takes a chunk of Markdown and
    turns it into an HTML block
    """

    blocks = markdown_to_blocks(doc)

    nodes = []

    for block in blocks:
        block_type = block_to_block_type(block)

        node = (block_type, block)
        nodes.append(node)

    print(f"nodes ${nodes}")
