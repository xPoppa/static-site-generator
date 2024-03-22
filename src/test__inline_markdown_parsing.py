import unittest

from textnode import (
        TextNode,
        text_type_text,
        text_type_bold,
        text_type_image,
        text_type_link,
        text_type_code,
        text_type_italic
        )
from inline_markdown_parsing import extract_markdown_images, extract_markdown_links, split_nodes_delimiter, split_nodes_image, split_nodes_links, text_to_textnodes

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


class TestImageSplitting(unittest.TestCase):
    def test_split_nodes_image(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            text_type_text,
        )
        new_nodes = split_nodes_image([node])

        self.assertListEqual(
            [
                TextNode("This is text with an ", text_type_text),
                TextNode("image", text_type_image, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", text_type_text),
                TextNode(
                    "second image", text_type_image, "https://i.imgur.com/3elNhQu.png"
                ),
            ], new_nodes
                )
    def test_split_nodes_image_diff_order(self):
        node1 = TextNode(
            "![image](https://i.imgur.com/zjjcJKZ.png) This is text with an and another ![second image](https://i.imgur.com/3elNhQu.png)",
            text_type_text,
        )
        new_nodes1 = split_nodes_image([node1])
        self.assertListEqual(
            [
                TextNode("image", text_type_image, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" This is text with an and another ", text_type_text),
                TextNode(
                    "second image", text_type_image, "https://i.imgur.com/3elNhQu.png"
                ),
            ], new_nodes1

            )
    def test_split_nodes_image_no_image(self):
        node = TextNode(text="haai ik heb geen image", text_type=text_type_text)
        new_nodes = split_nodes_image([node])
        self.assertListEqual([node], new_nodes)

    def test_only_image(self):
        node = TextNode(text="![image](https://i.imgur.com/zjjcJKZ.png)", text_type=text_type_text)
        new_nodes = split_nodes_image([node])
        self.assertListEqual([TextNode(text="image", text_type=text_type_image, url="https://i.imgur.com/zjjcJKZ.png")], new_nodes)

    def test_wrong_image_syntax(self):
        node = TextNode(text="!image](https://i.imgur.com/zjjcJKZ.png) This is text with an and another ![second image](https://i.imgur.com/3elNhQu.png)", text_type=text_type_text)
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
                [
                    TextNode(text="!image](https://i.imgur.com/zjjcJKZ.png) This is text with an and another ", text_type=text_type_text),
                    TextNode(text="second image", text_type=text_type_image, url="https://i.imgur.com/3elNhQu.png")
                ], new_nodes)
    def test_whitespace_and_image(self):
        node = TextNode(text="![image](https://i.imgur.com/zjjcJKZ.png)      ", text_type=text_type_text)
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
                [
                    TextNode(text="image", text_type=text_type_image, url="https://i.imgur.com/zjjcJKZ.png"),
                    TextNode(text="      ", text_type=text_type_text)
                ], new_nodes)

    def test_two_same_images(self):
        node = TextNode(text="![image](https://i.imgur.com/zjjcJKZ.png) lala ![image](https://i.imgur.com/zjjcJKZ.png)", text_type=text_type_text)
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
                [
                    TextNode(text="image", text_type=text_type_image, url="https://i.imgur.com/zjjcJKZ.png"),
                    TextNode(text=" lala ", text_type=text_type_text),
                    TextNode(text="image", text_type=text_type_image, url="https://i.imgur.com/zjjcJKZ.png")
                ], new_nodes
                )

    def test_two_same_images_next(self):
        node = TextNode(text="![image](https://i.imgur.com/zjjcJKZ.png)![image](https://i.imgur.com/zjjcJKZ.png)", text_type=text_type_text)
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
                [
                    TextNode(text="image", text_type=text_type_image, url="https://i.imgur.com/zjjcJKZ.png"),
                    TextNode(text="image", text_type=text_type_image, url="https://i.imgur.com/zjjcJKZ.png")
                ], new_nodes
                )
    def test_markdown_image_with_special_characters(self):
            # Creating a TextNode with markdown syntax that has special characters in the alt text
            # and a URL with parentheses. Using raw-string to avoid escaping issues.
            input_text = TextNode(r"This is an image with special characters: ![$peci@l Ch@ract3rs](http://example.com/image.png?foo=1&bar=(2)) in the alt text and URL.", text_type_text)

            # Calling split_nodes_image function with the input TextNode
            result = split_nodes_image([input_text])

            # Checking if the result is as expected
            expected_result = [
                TextNode("This is an image with special characters: ", text_type_text),
                TextNode("$peci@l Ch@ract3rs", text_type_image, url="http://example.com/image.png?foo=1&bar=(2"),
                TextNode(") in the alt text and URL.", text_type=text_type_text)
            ]
            self.assertListEqual(expected_result, result)

class TestLinkSplitting(unittest.TestCase):
    def test_split_nodes_links(self):
        node = TextNode(
            "This is text with an [link](https://i.imgur.com/zjjcJKZ.png) and another [second link](https://i.imgur.com/3elNhQu.png)",
            text_type_text,
        )
        new_nodes = split_nodes_links([node])

        self.assertListEqual(
            [
                TextNode("This is text with an ", text_type_text),
                TextNode("link", text_type_link, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", text_type_text),
                TextNode(
                    "second link", text_type_link, "https://i.imgur.com/3elNhQu.png"
                ),
            ], new_nodes
                )
    def test_split_nodes_links_diff_order(self):
        node1 = TextNode(
            "[link](https://i.imgur.com/zjjcJKZ.png) This is text with an and another [second link](https://i.imgur.com/3elNhQu.png)",
            text_type_text,
        )
        new_nodes1 = split_nodes_links([node1])
        self.assertListEqual(
            [
                TextNode("link", text_type_link, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" This is text with an and another ", text_type_text),
                TextNode(
                    "second link", text_type_link, "https://i.imgur.com/3elNhQu.png"
                ),
            ], new_nodes1

            )
    def test_split_nodes_links_no_link(self):
        node = TextNode(text="haai ik heb geen link", text_type=text_type_text)
        new_nodes = split_nodes_links([node])
        self.assertListEqual([node], new_nodes)

    def test_only_link(self):
        node = TextNode(text="[link](https://i.imgur.com/zjjcJKZ.png)", text_type=text_type_text)
        new_nodes = split_nodes_links([node])
        self.assertListEqual([TextNode(text="link", text_type=text_type_link, url="https://i.imgur.com/zjjcJKZ.png")], new_nodes)

    def test_wrong_link_syntax(self):
        node = TextNode(text="link](https://i.imgur.com/zjjcJKZ.png) This is text with an and another [second link](https://i.imgur.com/3elNhQu.png)", text_type=text_type_text)
        new_nodes = split_nodes_links([node])
        self.assertListEqual(
                [
                    TextNode(text="link](https://i.imgur.com/zjjcJKZ.png) This is text with an and another ", text_type=text_type_text),
                    TextNode(text="second link", text_type=text_type_link, url="https://i.imgur.com/3elNhQu.png")
                ], new_nodes)
    def test_whitespace_and_link(self):
        node = TextNode(text="[link](https://i.imgur.com/zjjcJKZ.png)      ", text_type=text_type_text)
        new_nodes = split_nodes_links([node])
        self.assertListEqual(
                [
                    TextNode(text="link", text_type=text_type_link, url="https://i.imgur.com/zjjcJKZ.png"),
                    TextNode(text="      ", text_type=text_type_text)
                ], new_nodes)

    def test_two_same_links(self):
        node = TextNode(text="[link](https://i.imgur.com/zjjcJKZ.png) lala [link](https://i.imgur.com/zjjcJKZ.png)", text_type=text_type_text)
        new_nodes = split_nodes_links([node])
        self.assertListEqual(
                [
                    TextNode(text="link", text_type=text_type_link, url="https://i.imgur.com/zjjcJKZ.png"),
                    TextNode(text=" lala ", text_type=text_type_text),
                    TextNode(text="link", text_type=text_type_link, url="https://i.imgur.com/zjjcJKZ.png")
                ], new_nodes
                )

    def test_two_same_links_next(self):
        node = TextNode(text="[link](https://i.imgur.com/zjjcJKZ.png)[link](https://i.imgur.com/zjjcJKZ.png)", text_type=text_type_text)
        new_nodes = split_nodes_links([node])
        self.assertListEqual(
                [
                    TextNode(text="link", text_type=text_type_link, url="https://i.imgur.com/zjjcJKZ.png"),
                    TextNode(text="link", text_type=text_type_link, url="https://i.imgur.com/zjjcJKZ.png")
                ], new_nodes
                )
    def test_markdown_link_with_special_characters(self):
            # Creating a TextNode with markdown syntax that has special characters in the alt text
            # and a URL with parentheses. Using raw-string to avoid escaping issues.
            input_text = TextNode(r"This is an link with special characters: [$peci@l Ch@ract3rs](http://example.com/link.png?foo=1&bar=(2)) in the alt text and URL.", text_type_text)

            # Calling split_nodes_links function with the input TextNode
            result = split_nodes_links([input_text])

            # Checking if the result is as expected
            expected_result = [
                TextNode("This is an link with special characters: ", text_type_text),
                TextNode("$peci@l Ch@ract3rs", text_type_link, url="http://example.com/link.png?foo=1&bar=(2"),
                TextNode(") in the alt text and URL.", text_type_text)
            ]
            self.assertListEqual(expected_result, result)

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

class TextToNodes(unittest.TestCase):
    def test_text_extracting(self):
       nodes = text_to_textnodes("This is **text** with an *italic* word and a `code block` and an ![image](https://i.imgur.com/zjjcJKZ.png) and a [link](https://boot.dev)")
       expected_nodes =([
                            TextNode("This is ", text_type_text),
                            TextNode("text", text_type_bold),
                            TextNode(" with an ", text_type_text),
                            TextNode("italic", text_type_italic),
                            TextNode(" word and a ", text_type_text),
                            TextNode("code block", text_type_code),
                            TextNode(" and an ", text_type_text),
                            TextNode("image", text_type_image, "https://i.imgur.com/zjjcJKZ.png"),
                            TextNode(" and a ", text_type_text),
                            TextNode("link", text_type_link, "https://boot.dev")
                        ])
       self.assertListEqual(nodes, expected_nodes)




if __name__ == "__main__":
    unittest.main()

