import unittest

from block_markdown_parsing import (
        block_to_block_type,
        markdown_to_blocks,
        block_type_heading,
        block_type_paragraph,
        block_type_quote,
        block_type_code,
        block_type_unordered_list,
        block_type_ordered_list
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

    def test_to_block_quote(self):
        block_type = block_to_block_type(">lalala\n>lalalla\n>lalalla\n>lallala")
        block_type1 = block_to_block_type(">lalala\nlalalla\n>lalalla\n>lallala")
        self.assertEqual(block_type, block_type_quote)
        self.assertEqual(block_type1, block_type_paragraph)

    def test_to_block_code(self):
        block_type = block_to_block_type("""```this is some code bro and it goes on for ever i dont where i need to split it Where should i break it up? I ha
Now i continue here so i can have thus on big code block```""")
        self.assertEqual(block_type, block_type_code)

    def test_to_block_unordered_list(self):
        block_type = block_to_block_type("* This is a list\n* with items\n* items")
        self.assertEqual(block_type, block_type_unordered_list)
        block_type2 = block_to_block_type("- This is a list\n- with items\n- items")
        self.assertEqual(block_type2, block_type_unordered_list)

    def test_to_block_ordered_list(self):
        block_type = block_to_block_type("1. This is a list\n2. with items\n3. items")
        self.assertEqual(block_type, block_type_ordered_list)



if __name__ == "__main__":
    unittest.main()
