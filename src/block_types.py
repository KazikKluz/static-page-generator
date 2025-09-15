"""This module contains method for transforming block into specific HTML block"""

import re
from enum import Enum


class BlockType(Enum):
    """Only this type of blocks are allowed"""

    PARAGRAPH = "p"
    H1 = "h1"
    H2 = "h2"
    H3 = "h3"
    H4 = "h4"
    H5 = "h5"
    H6 = "h6"
    CODE = "code"
    QUOTE = "blockquote"
    ULIST = "ul"
    OLIST = "ol"


def block_to_block_type(block):
    """Trasforms block to block type"""
    lead = block.split(" ", 1)[0].replace("\n", "")
    tail = block.rsplit(" ", 1)[1].replace("\n", "")

    match lead:
        case "#":
            return BlockType.H1
        case "##":
            return BlockType.H2
        case "###":
            return BlockType.H3
        case "####":
            return BlockType.H4
        case "#####":
            return BlockType.H5
        case "######":
            return BlockType.H6
        case "```":
            if tail == "```":
                return BlockType.CODE
            return BlockType.PARAGRAPH
        case ">":
            return BlockType.QUOTE
        case _ if re.fullmatch(r"\d+\.", lead):
            return BlockType.OLIST
        case "-":
            return BlockType.ULIST
        case _:
            return BlockType.PARAGRAPH
