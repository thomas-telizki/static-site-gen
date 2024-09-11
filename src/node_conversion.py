#!/usr/bin/env python3

from textnode import *
from leafnode import *
import re

def text_node_to_html_node(text_node):

    match(text_node.text_type):
        case TextType.TEXT:
            return LeafNode(text_node.text)

        case TextType.BOLD:
            return LeafNode(text_node.text, "b")

        case TextType.ITALIC:
            return LeafNode(text_node.text, "i")

        case TextType.CODE:
            return LeafNode(text_node.text, "code")

        case TextType.LINK:
            return LeafNode(text_node.text, "a", text_node.url)

        case TextType.IMG:
            return LeafNode("", "img", {"src": text_node.url, "alt": text_node.text})

        case _:
            raise Exception("Unknown TextNode Type")

def split_nodes_delimiter(old_nodes, delimiter, text_type: TextType):

    new_nodes = []

    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        split_nodes = []
        sections = node.text.split(delimiter)

        if len(sections) % 2 == 0:
           raise ValueError("Invalid markdown, formatted sections not closed")

        for i in range(len(sections)):
            if sections[i] == "":
                continue

            if i % 2 == 0:
                split_nodes.append(TextNode(sections[i], TextType.TEXT))
            else:
                split_nodes.append(TextNode(sections[i], text_type))
        new_nodes.extend(split_nodes)
    return new_nodes

def extract_markdown_images(text):
    return re.findall(r'!\[(.*?)\]\((.*?)\)', text)

def extract_markdown_links(text):
    return re.findall(r'\[(.*?)\]\((.*?)\)', text)
