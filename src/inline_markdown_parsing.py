from textnode import (
        TextNode,
        text_type_text,
#        text_type_bold,
#        text_type_image,
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
    for node in nodes:
        matches = extract_markdown_images(node.text)
        lala = []
        for m in matches:
            some_text = node.text.split(f"![{m[0]}]({m[1]})")
            lala.append(some_text[0])
        print(f"print lala: {lala}")
        return []
    return []

def recurse(tuple_list, text_list):
    if len(tuple_list) == 0:
        return
    m = tuple_list[0]
    text_list[0].split(f"![{m[0]}]({m[1]})") 
    return 
