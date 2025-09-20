"""The module extracts a title from the Markdown document"""

from src.split_blocks import markdown_to_blocks
from src.block_types import block_to_block_type


def extract_title(markdown):
    """Gets h1 title from Markdown"""

    blocks = markdown_to_blocks(markdown)
    title = ""

    for block in blocks:
        split = block.split(" ", 1)
        if block_to_block_type(block).value == "h" and len(split[0].replace("\n", "")) == 1:
            title += split[1].replace("\n", "")
            break

    if len(title) == 0:
        raise ValueError("Invalid Markdown - No Title")

    return title
