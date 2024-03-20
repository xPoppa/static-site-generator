import unittest

from textnode import (
        TextNode,
        text_type_text,
        text_type_bold,
#        text_type_image,
#        text_type_link,
        text_type_code,
        text_type_italic
        )
from inline_markdown_parsing import extract_markdown_images, extract_markdown_links, split_nodes_delimiter, split_nodes_image

class TestSplittingNodes(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is text with a `code block` word", text_type_text)
        splitted_nodes = split_nodes_delimiter([node], "`", text_type_code)
        test_splitted_nodes = [
                    TextNode(text="This is text with a ", text_type=text_type_text),
                    TextNode(text="code block", text_type=text_type_code),
                    TextNode(text=" word", text_type=text_type_text)
                ]
        self.assertEqual(splitted_nodes, test_splitted_nodes)


        node1 = TextNode("This is text with a `code block` word `another code block`", text_type_text)
        splitted_nodes1 = split_nodes_delimiter([node1], "`", text_type_code)
        test_splitted_nodes1 = [
                    TextNode(text="This is text with a ", text_type=text_type_text),
                    TextNode(text="code block", text_type=text_type_code),
                    TextNode(text=" word ", text_type=text_type_text),
                    TextNode(text="another code block", text_type=text_type_code),
                ]
        self.assertEqual(splitted_nodes1, test_splitted_nodes1)

        node2 = TextNode("This is text with a **bold** word", text_type_text)
        splitted_nodes2 = split_nodes_delimiter([node2], "**", text_type_bold)
        test_splitted_nodes2 = [
                    TextNode(text="This is text with a ", text_type=text_type_text),
                    TextNode(text="bold", text_type=text_type_bold),
                    TextNode(text=" word", text_type=text_type_text),
                ]
        self.assertEqual(splitted_nodes2, test_splitted_nodes2)


        node3 = TextNode("This is text with a *italic* word", text_type_text)
        splitted_nodes3 = split_nodes_delimiter([node3], "*", text_type_italic)
        test_splitted_nodes3 = [
                    TextNode(text="This is text with a ", text_type=text_type_text),
                    TextNode(text="italic", text_type=text_type_italic),
                    TextNode(text=" word", text_type=text_type_text),
                ]
        self.assertEqual(splitted_nodes3, test_splitted_nodes3)
    
    def test_split_nodes_image(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            text_type_text,
        )
        new_nodes = split_nodes_image([node])
        

class TestExtractLink(unittest.TestCase):
    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_extract_markdown_links(self):
        matches = extract_markdown_links(
            "This is text with a [link](https://boot.dev) and [another link](https://blog.boot.dev)"
        )
        self.assertListEqual(
            [
                ("link", "https://boot.dev"),
                ("another link", "https://blog.boot.dev"),
            ],
            matches,
        )


if __name__ == "__main__":
    unittest.main()