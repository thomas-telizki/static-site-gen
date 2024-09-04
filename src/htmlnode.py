#!/usr/bin/env python3
import json

class HTMLNode:

    def __init__(self, value=None, tag=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError()

    def props_to_html(self):
        str = ""

        for prop in self.props:
            str += f'{prop}="{self.props[prop]}" '

        return " " + str.strip()

    def __repr__(self):
       return json.dumps({
            "name": "HTMLNode",
            "tag": self.tag,
            "value": self.value,
            "children": self.children,
            "props": self.props
        })
