"""This module contains method for transforming block into specific HTML block"""

import re
from enum import Enum


class BlockType(Enum):
    """Only this type of blocks are allowed"""

    PARAGRAPH = "p"
    HEADER = "h"
    CODE = "code"
    QUOTE = "blockquote"
    ULIST = "ul"
    OLIST = "ol"


def block_to_block_type(block):
    """Trasforms block to block type"""
    lead = block.split(" ", 1)[0].replace("\n", "")
    tail = block.rsplit(" ", 1)[1].replace("\n", "")

    match lead:
        case "#" | "##" | "###" | "####" | "#####" | "######":
            return BlockType.HEADER
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
