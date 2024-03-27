from htmlnode import HtmlNode, LeafNode, ParentNode
from block_markdown_parsing import (
        block_to_block_type,
        block_type_heading,
        block_type_paragraph,
        block_type_quote,
        block_type_code,
        block_type_unordered_list,
        block_type_ordered_list,
        markdown_to_blocks
        )
from inline_markdown_parsing import text_to_textnodes
from textnode import text_node_to_html_node


def markdown_to_html(text: str) -> ParentNode:
    # cut text in blocks
    blocks = markdown_to_blocks(text)
    children = [] 
    for block in blocks:
        block_type = block_to_block_type(block)
        if block_type == block_type_heading:
            children.append(heading_block_to_html_node(block))
        if block_type == block_type_quote:
            children.append(quote_block_to_html_node(block))
        if block_type == block_type_code:
            children.append(code_block_to_html_node(block))
        if block_type == block_type_unordered_list:
            children.append(ul_block_to_html_node(block))
        if block_type == block_type_ordered_list:
            children.append(ol_block_to_html_node(block))
        if block_type == block_type_paragraph:
            children.append(par_block_to_html_node(block))
    return ParentNode(tag="div", children=children)

def heading_block_to_html_node(block: str) -> LeafNode:
    if block.startswith("# "):
        return LeafNode(tag="h1", value=block[2:])
    if block.startswith("## "):
        return LeafNode(tag="h2", value=block[3:])
    if block.startswith("### "):
        return LeafNode(tag="h3", value=block[4:])
    if block.startswith("#### "):
        return LeafNode(tag="h4", value=block[5:])
    if block.startswith("##### "):
        return LeafNode(tag="h5", value=block[6:])
    if block.startswith("###### "):
        return LeafNode(tag="h6", value=block[7:])
    return LeafNode()


def quote_block_to_html_node(block: str) -> ParentNode:
    return ParentNode(tag="blockquote", 
                      children=
                        text_to_leaf_nodes(block.replace(">", "").replace("\n", "").strip()))

def code_block_to_html_node(block: str) -> ParentNode:
    return ParentNode(tag="pre", 
                      children=to_code_nodes(block[3:-3]))

def to_code_nodes(text: str) -> list[LeafNode]:
    splitted_text = text.split("\n")
    leaf_nodes: list[LeafNode] = []
    for t in splitted_text:
        leaf_nodes.append(LeafNode(tag="code", value=t))
    return leaf_nodes


def ul_block_to_html_node(block: str) -> ParentNode:
    return ParentNode(tag="ul", children=map(to_ul_list_item,block.split("\n")))


def ol_block_to_html_node(block: str) -> ParentNode:
    return ParentNode(tag="ol", 
                      children=map(to_ol_list_item, block.split("\n")))
def par_block_to_html_node(block: str) -> ParentNode:
    lines = block.split("\n")
    paragraph = " ".join(lines)
    children = text_to_leaf_nodes(paragraph)
    return ParentNode(tag="p", children=children)

            ##### HELPERS ######
def text_to_leaf_nodes(text: str) -> list[LeafNode]:
    text_nodes = text_to_textnodes(text)
    leaf_nodes = []
    for text_node in text_nodes:
        leaf_nodes.append(text_node_to_html_node(text_node))
    return leaf_nodes

def to_ul_list_item(item: str) -> HtmlNode:
    list_item = item[1:] 
    return ParentNode(tag="li", children=text_to_leaf_nodes(list_item.strip()))

def to_ol_list_item(item: str) -> HtmlNode:
    list_item = item[2:] 
    return ParentNode(tag="li", children=text_to_leaf_nodes(list_item.strip()))

def strip(text: str) -> str:
    return text.strip()
