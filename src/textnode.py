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

    def __eq__(self, other):
        return (
            self.text == other.text
            and self.text_type.value == other.text_type.value
            and self.url == other.url
            )

    def __repr__(self):
        return json.dumps({
            "name": "TextNode",
            "text": self.text,
            "text_type": self.text_type.value,
            "url": self.url
        })
