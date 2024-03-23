import unittest

from block_markdown_parsing import (
        block_to_block_type,
        markdown_to_blocks,
        block_type_heading,
        block_type_paragraph
        )


class TestToBlocks(unittest.TestCase):
    def test_to_blocks(self):

        markdown = """
This is **bolded** paragraph

This is another paragraph with *italic* text and `code` here
This is the same paragraph on a new line


* This is a list
* with items
"""
        blocks = markdown_to_blocks(markdown)
        expected_blocks = [
                            "This is **bolded** paragraph",
                            "This is another paragraph with *italic* text and `code` here\nThis is the same paragraph on a new line",
                            "* This is a list\n* with items"


                          ]
        self.assertListEqual(blocks, expected_blocks)

    def test_markdown_to_blocks_newlines(self):
        md = """
This is **bolded** paragraph






This is another paragraph with *italic* text and `code` here
This is the same paragraph on a new line



* This is a list
* with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with *italic* text and `code` here\nThis is the same paragraph on a new line",
                "* This is a list\n* with items",
            ],
        )

class TestToBlockTypes(unittest.TestCase):
    def test_to_block_type_header(self):
        block_type = block_to_block_type("# miauw")
        block_type2 = block_to_block_type("## miauw")
        block_type3 = block_to_block_type("### miauw")
        block_type4 = block_to_block_type("#### miauw")
        block_type5 = block_to_block_type("##### miauw")
        block_type6 = block_to_block_type("###### miauw")
        block_type_wrong = block_to_block_type("####### miauw")
        self.assertEqual(block_type, block_type_heading)
        self.assertEqual(block_type2, block_type_heading)
        self.assertEqual(block_type3, block_type_heading)
        self.assertEqual(block_type4, block_type_heading)
        self.assertEqual(block_type5, block_type_heading)
        self.assertEqual(block_type6, block_type_heading)
        self.assertEqual(block_type_wrong, block_type_paragraph)

if __name__ == "__main__":
    unittest.main()
