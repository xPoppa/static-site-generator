import unittest

from block_markdown_parsing import markdown_to_blocks


class TestToBlocks(unittest.TestCase):
    markdown = """This is **bolded** paragraph

This is another paragraph with *italic* text and `code` here
This is the same paragraph on a new line

* This is a list
 * with items"""

    print(f"The markdown: \n {markdown}")
    blocks = markdown_to_blocks(markdown)
    print(blocks)
