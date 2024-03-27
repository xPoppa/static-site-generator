import shutil
import os
from block_markdown_parsing import (block_to_block_type, markdown_to_blocks,
                                    block_type_heading
                                    )
from markdown_to_html import markdown_to_html

def extract_title(markdown: str):
    blocks = markdown_to_blocks(markdown)
    headings = []
    for block in blocks:
        block_type = block_to_block_type(block)
        if block_type == block_type_heading:
            headings.append(block)
    for heading in headings:
        if heading.startswith("# "):
            return heading[2:]
    raise Exception("h1 is necessary for markdown!!!!")


def generate_page(from_path: str, template_path: str, dest_path: str) -> None:
    print("Generating page from from_path to dest_path using template_path")

    markdown_file = open(from_path, "r")
    markdown = markdown_file.read()
    markdown_file.close()

    template_file = open(template_path, "r")
    template = template_file.read()
    template_file.close()

    html = markdown_to_html(markdown).to_html()

    title = extract_title(markdown)
    template = template.replace("{{ Title }}", title)

    template = template.replace("{{ Content }}", html)
    dirname = os.path.dirname(dest_path)
    if not os.path.exists(dirname): os.makedirs(dirname)
    new_html_file = open(dest_path, "w")
    new_html_file.write(template)
    new_html_file.close()

def generate_page_recursive(
        dir_path_content: str, 
        template_path: str, 
        dest_dir_path: str
        )-> None:
    print(f"Generating pages from {dir_path_content} to {dest_dir_path} using template_path")
    if os.path.exists(dest_dir_path):
        shutil.rmtree(dest_dir_path)
    if not os.path.exists(dest_dir_path):
        os.mkdir(dest_dir_path)
    for filename in os.listdir(dir_path_content):
        from_path = os.path.join(dir_path_content, filename)
        dest_path = os.path.join(dest_dir_path, filename)
        if os.path.isfile(from_path):
            if filename.endswith(".md"):
                generate_page(from_path,template_path,dest_path.replace(".md", ".html"))
        else: generate_page_recursive(from_path, template_path, dest_path)

