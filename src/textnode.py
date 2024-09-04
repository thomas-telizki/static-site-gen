#!/usr/bin/env python3
from enum import Enum
import json


class TextType(Enum):
    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMG = "image"

class TextNode:

    def __init__(self, text, text_type: TextType, url = None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eg__(self, other):
        return (
            self.text == other.text
            and self.text_type == other.text_type
            and self.url == other.url
            )

    def __repr__(self):
        return f'{{"name": TextNode, "text": {self.text}, "text_type": {self.text_type.value}, "url": {self.url}}}'
