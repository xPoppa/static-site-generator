import unittest
from htmlnode import LeafNode

from markdown_to_html import (
        code_block_to_html_node,
        heading_block_to_html_node,
        markdown_to_html,
        ol_block_to_html_node,
        quote_block_to_html_node,
        ul_block_to_html_node
        )


class TestHeading(unittest.TestCase):
    def test_heading_to_html(self):
        heading_node = heading_block_to_html_node("# This is the heading").to_html()
        expected_node = LeafNode(tag="h1", value="This is the heading").to_html()
        self.assertEqual(heading_node, expected_node)


class TestQuoteblock(unittest.TestCase):
    def test_quote_block(self):
        quote_block_node = quote_block_to_html_node("> i am a quote block\n> new quote block\n> another quote block").to_html()
        expected_node = "<blockquote>i am a quote block new quote block another quote block</blockquote>"
        self.assertEqual(quote_block_node, expected_node)
    
    def empty_quote_block(self):
        quote_block_node = quote_block_to_html_node("> \n> text\n> text")
        expected_node = "<blockquote>  test test</blockquote>"
        self.assertEqual(quote_block_node, expected_node)

class TestCodeBlock(unittest.TestCase):
    def test_code_block(self):
        code_block_node = code_block_to_html_node("```console.log(45)```").to_html()
        expected_node = "<pre><code>console.log(45)</code></pre>"
        self.assertEqual(code_block_node, expected_node)

    def test_code_block_new_lines(self):
        code_block_node = code_block_to_html_node("```console.log(45)\n for x in xs {\nif x === y return y}\n else return x```").to_html()
        expected_node = "<pre><code>console.log(45)</code><code> for x in xs {</code><code>if x === y return y}</code><code> else return x</code></pre>"
        self.assertEqual(code_block_node, expected_node)

class TestUL(unittest.TestCase):
    def test_ul_block(self):
        ul_block_node = ul_block_to_html_node("* haha\n* haha\n* haha").to_html()
        expected_node = "<ul><li>haha</li><li>haha</li><li>haha</li></ul>"
        self.assertEqual(ul_block_node, expected_node)

class TestOL(unittest.TestCase):
    def test_ul_block(self):
        ul_block_node = ol_block_to_html_node("1. haha\n2. haha\n3. haha").to_html()
        expected_node = "<ol><li>haha</li><li>haha</li><li>haha</li></ol>"
        self.assertEqual(ul_block_node, expected_node)


class TestMarkdownParsing(unittest.TestCase):
    def test_paragraph(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

"""
    
        node = markdown_to_html(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p></div>",
        )
    
    def test_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with *italic* text and `code` here

"""
    
        node = markdown_to_html(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )
    
    def test_lists(self):
        md = """
- This is a list
- with items
- and *more* items

1. This is an `ordered` list
2. with items
3. and more items

"""
    
        node = markdown_to_html(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ul><li>This is a list</li><li>with items</li><li>and <i>more</i> items</li></ul><ol><li>This is an <code>ordered</code> list</li><li>with items</li><li>and more items</li></ol></div>",
        )
    
    def test_headings(self):
        md = """
# this is an h1

this is paragraph text

## this is an h2
"""
    
        node = markdown_to_html(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h1>this is an h1</h1><p>this is paragraph text</p><h2>this is an h2</h2></div>",
        )
    
    def test_blockquote(self):
        md = """
> This is a
> blockquote block

this is paragraph text

"""
    
        node = markdown_to_html(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><blockquote>This is a blockquote block</blockquote><p>this is paragraph text</p></div>",
        )
