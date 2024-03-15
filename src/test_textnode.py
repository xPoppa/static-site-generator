import unittest

from textnode import TextNode


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)
        node3 = TextNode("miauw", "italic", "www.lala.com")
        node4 = TextNode("miauw", "italic", "www.lala.com")
        node5 = TextNode("This is a text node", "bold", "www.google.com")
        self.assertEqual(node3, node4)
        self.assertNotEqual(node,node3)
        self.assertNotEqual(node, node5)


if __name__ == "__main__":
    unittest.main()
