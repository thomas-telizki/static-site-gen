#!/usr/bin/env python3

from htmlnode import *

class LeafNode(HTMLNode):

    def __init__(self, value, tag=None, props=None):
        super().__init__(value, tag, None, props)
        self.value = value
        self.tag = tag
        self.props = props

    def to_html(self):
        if self.value is None:
            raise ValueError("LeafNode must have value")

        if self.tag is None:
            return self.value

        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
