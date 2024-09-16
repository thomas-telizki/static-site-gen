#!/usr/bin/env python3
from enum import Enum
import re

class BlockType(Enum):
    PARA = "paragraph"
    HEAD = "^(#{1,6})\s(.+)$"
    CODE = "code"
    QUOTE = "quote"
    ULIST = "unordered_list"
    OLIST = "ordered_list"

def markdown_to_blocks(markdown):
    sections = markdown.split("\n\n")
    blocks = []

    for s in sections:

        if s == "":
            continue

        s = s.strip()
        blocks.append(s)

    return blocks

def block_to_block_type(block):

    if re.compile(r'^(#{1,6})\s(.+)$').match(block):
        return BlockType.HEAD

    if re.compile(r'```[\s\S]*?```').match(block):
        return BlockType.CODE

    if re.compile(r'^>\s?.*$', re.MULTILINE).match(block):
        return BlockType.QUOTE

    if re.compile(r'^(?:\s*(?:\*|-)\s.+\r?\n)*\s*(?:\*|-)\s.+$', re.MULTILINE).match(block):
        return BlockType.ULIST

    if re.compile(r'^\s*(\d+)\.\s.+$', re.MULTILINE).match(block):
        return BlockType.OLIST

    return BlockType.PARA
