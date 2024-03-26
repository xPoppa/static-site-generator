from htmlnode import HtmlNode, LeafNode, ParentNode
from block_markdown_parsing import (
        block_type_heading,
        block_type_paragraph,
        block_type_quote,
        block_type_code,
        block_type_unordered_list,
        block_type_ordered_list
        )
from inline_markdown_parsing import text_to_textnodes
from textnode import text_node_to_html_node

def heading_block_to_html_node(block: str) -> HtmlNode:
    if block.startswith("# "):
        return HtmlNode(tag="h1", value=block[2:])
    if block.startswith("## "):
        return HtmlNode(tag="h2", value=block[3:])
    if block.startswith("### "):
        return HtmlNode(tag="h3", value=block[4:])
    if block.startswith("#### "):
        return HtmlNode(tag="h4", value=block[5:])
    if block.startswith("##### "):
        return HtmlNode(tag="h5", value=block[6:])
    if block.startswith("###### "):
        return HtmlNode(tag="h6", value=block[7:])
    return HtmlNode()

def text_to_leaf_nodes(text: str) -> list[LeafNode]:
    text_nodes = text_to_textnodes(text)
    leaf_nodes = []
    for text_node in text_nodes:
        leaf_nodes.append(text_node_to_html_node(text_node))
    return leaf_nodes

def quote_block_to_html_node(block: str) -> HtmlNode:
    return ParentNode(tag="blockquote", children=text_to_leaf_nodes(block.strip(">")))

def code_block_to_html_node(block: str) -> HtmlNode:
    return HtmlNode(tag="code", value=block[3:-3])

def ul_block_to_html_node(block: str) -> HtmlNode:
    return HtmlNode(tag="ul", children=map(to_ul_list_item,block.split("\n")))

def to_ul_list_item(item: str) -> HtmlNode:
    list_item = item[1:] 
    return HtmlNode(tag="li", value=list_item)

def to_ol_list_item(item: str) -> HtmlNode:
    list_item = item[1:] 
    return HtmlNode(tag="li", value=list_item)

def ol_block_to_html_node(block: str) -> HtmlNode:
    return HtmlNode(tag="ol", children=map(to_ol_list_item, block.split("\n")))
