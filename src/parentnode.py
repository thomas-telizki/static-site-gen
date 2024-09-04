#!/usr/bin/env python3

from htmlnode import *

class ParentNode(HTMLNode):

    def __init__(self, tag, children, props=None):
        super().__init__(None, tag, children, props)
        self.tag = tag
        self.children = children
        self.props = props

    def to_html(self):
        if self.tag is None:
            raise ValueError("ParentNode must have tag")

        if len(self.children) == 0 or self.children is None:
            raise ValueError("ParentNode must have children")

        children_str = ""

        for child in self.children:
            children_str += child.to_html()

        return f"<{self.tag}{self.props_to_html()}>{children_str}</{self.tag}>"
