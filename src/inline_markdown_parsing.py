from textnode import (
        TextNode,
        text_type_text,
#        text_type_bold,
        text_type_image,
#        text_type_link,
#        text_type_code,
#        text_type_italic
        )
import re

def split_nodes_delimiter(old_nodes: list[TextNode], delimiter: str, text_type: str) -> list[TextNode]:
    nodes_list = []
    for node in old_nodes:
        if not isinstance(node, TextNode):
            nodes_list.extend(node)
            continue
        idx = node.text.find(delimiter)
        idx2 = node.text.find(delimiter, idx + 1)
        if idx2 == -1:
            raise Exception("Invalid markdown syntax closing delimiter not found")
        splitted_text = node.text.split(delimiter)
        nodes = []
        for idx, text in enumerate(splitted_text):
            if idx == 0:
                nodes.append(TextNode(text=text, text_type=text_type_text))
            elif idx % 2 != 0:
                nodes.append(TextNode(text=text, text_type=text_type))
            elif text == "":
                continue
            else:nodes.append(TextNode(text=text, text_type=text_type_text))
        nodes_list += nodes
    return nodes_list

def extract_markdown_images(text: str) -> list[tuple[str, str]]:
    return re.findall(r"!\[(.*?)\]\((.*?)\)", text)

def extract_markdown_links(text: str) -> list[tuple[str,str]]:
    return re.findall(r"\[(.*?)\]\((.*?)\)", text)

def split_nodes_image(nodes: list[TextNode]) -> list[TextNode]:
    nodes_list = []
    for node in nodes:
        matches = extract_markdown_images(node.text)
        if len(matches) == 0 :
            nodes_list.extend([node])
            continue
        text_nodes = recurse(matches, [], node.text)
        nodes_list.extend(text_nodes)
    return nodes_list

def recurse(tuple_list: list[tuple[str,str]], acc: list[TextNode], text: str):
    if len(tuple_list) == 0:
        return acc
    m = tuple_list[0]
    splitted: list[str] = text.split(f"![{m[0]}]({m[1]})", 1) 
    if splitted[0] != "":
        acc.append(TextNode(text=splitted[0], text_type=text_type_text))
    acc.append(TextNode(text=m[0], text_type=text_type_image, url=m[1]))
    return recurse(tuple_list[1:], acc, splitted[1]) 
