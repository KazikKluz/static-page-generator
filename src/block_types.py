"""This module contains method for transforming block into specific HTML block"""

import re
from enum import Enum


class BlockType(Enum):
    """Only this type of blocks are allowed"""

    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    ULIST = "unordered_list"
    OLIST = "ordered_list"


def block_to_block_type(block):
    """Trasforms block to block type"""
    lead = block.split(" ", 1)[0]
    tail = block.rsplit(" ", 1)[1]

    match lead:
        case "#" | "##" | "###" | "####" | "#####" | "######":
            return BlockType.HEADING
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
