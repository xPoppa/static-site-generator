import unittest

from htmlnode import HtmlNode
from htmlnode import LeafNode
from htmlnode import ParentNode


class TestHtmlNode(unittest.TestCase):
    def test_eq(self):
        node = HtmlNode(tag="p", value="Hello there", props={"href": "https://www.google.com", "target": "_blank"})
        node1 = HtmlNode(tag="p", value="Hello there", props={"href": "https://www.google.com", "target": "_blank"})
        node2 = HtmlNode(tag="a", value="miauw", props={"href": "https://www.google.com", "target": "_blank"})
        self.assertEqual(node.props_to_html(), node1.props_to_html())
        self.assertEqual(node.props_to_html(), node2.props_to_html())
        node3 = HtmlNode(tag="a", value="miauw", props={"class": "bruv", "target": "_blank"})
        self.assertNotEqual(node2.props_to_html(), node3.props_to_html())


class TestLeafNode(unittest.TestCase):
    def test_eq(self):
        node = LeafNode(tag="p", value="Hello World")
        node1 = LeafNode(tag="p", value="Hello World")
        node2 = LeafNode(tag="a", value="Hello World",props={"href": "https://www.google.com", "target": "_blank"} )
        node3 = LeafNode("p", "This is a paragraph of text.")
        node4 = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), node1.to_html())
        self.assertEqual(node.to_html(), "<p>Hello World</p>")
        self.assertEqual(node2.to_html(), "<a href=\"https://www.google.com\" target=\"_blank\">Hello World</a>")
        self.assertEqual(node3.to_html(), "<p>This is a paragraph of text.</p>")
        self.assertEqual(node4.to_html(), "<a href=\"https://www.google.com\">Click me!</a>")

class TextParentNode(unittest.TestCase):
    def test_eq(self):
        node = ParentNode(
            tag="p",
            children=[
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        node2 = ParentNode(
                tag="div",
                children=[
                        ParentNode(
                            tag="div", 
                            children=
                                [
                                    LeafNode("b", "Bold text"),
                                    LeafNode(None, "Normal text"),
                                    LeafNode("i", "italic text"),
                                    LeafNode(None, "Normal text"),
                                ]
                        ),
                        LeafNode("b", "Bold text"),
                    ],
                )
        node3 = ParentNode(
                tag="div",
                children=[
                        ParentNode(
                            tag="div", 
                            children=
                                [
                                    LeafNode("b", "Bold text"),
                                    LeafNode(None, "Normal text"),
                                    LeafNode("i", "italic text"),
                                    LeafNode(None, "Normal text"),
                                ]
                        ),
                        LeafNode("b", "Bold text"),
                    ],
                props={"class": "bg-gray-200"}
                )
        node4 = ParentNode(
                tag="div",
                children=[
                        ParentNode(
                            tag="div", 
                            children=
                                [ ParentNode(
                                    tag="div",
                                    children=[
                                            ParentNode(
                                                tag="div", 
                                                children=
                                                    [
                                                        LeafNode("b", "Bold text"),
                                                        LeafNode(None, "Normal text"),
                                                        LeafNode("i", "italic text"),
                                                        LeafNode(None, "Normal text"),
                                                    ]
                                            ),
                                            LeafNode("b", "Bold text"),
                                    ],
                                )
                            ]
                        ),
                        LeafNode("b", "Bold text"),
                    ],
                props={"class": "bg-gray-200"}
                )
        self.assertEqual(node.to_html(), "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>")
        self.assertEqual(node2.to_html(), "<div><div><b>Bold text</b>Normal text<i>italic text</i>Normal text</div><b>Bold text</b></div>")
        self.assertEqual(node3.to_html(), "<div class=\"bg-gray-200\"><div><b>Bold text</b>Normal text<i>italic text</i>Normal text</div><b>Bold text</b></div>")
        self.assertEqual(node4.to_html(), "<div class=\"bg-gray-200\"><div><div><div><b>Bold text</b>Normal text<i>italic text</i>Normal text</div><b>Bold text</b></div></div><b>Bold text</b></div>")


if __name__ == "__main__":
    unittest.main()
