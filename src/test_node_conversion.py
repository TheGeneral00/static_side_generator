import unittest
from textnode import TextNode
from functions import text_node_to_html_node
from leafnode import LeafNode

class TestConversion(unittest.TestCase):
    def test(self):
        node = TextNode(text_type="text" , text="Hello")
        node2 = TextNode(text_type="bold" , text="Hello")
        node3 = TextNode(text_type="italic" , text="Hello")
        node4 = TextNode(text_type="code" , text="Hello")
        node5 = TextNode(text_type="link" , text="Hello" , url="http://example.com" )
        node6 = TextNode(text_type="image" , text="A picture" , url="http://example.com/image.jpg")
        node7 = TextNode(text_type="unknown" , text="Hello")
      
        self.assertEqual(text_node_to_html_node(node), LeafNode(value="Hello"))
        self.assertEqual(text_node_to_html_node(node2), LeafNode(tag="b", value="Hello"))
        self.assertEqual(text_node_to_html_node(node3), LeafNode(tag="i", value="Hello"))
        self.assertEqual(text_node_to_html_node(node4), LeafNode(tag="code", value="Hello"))
        self.assertEqual(text_node_to_html_node(node5), LeafNode(tag="a", value="Hello", props={"href": "http://example.com"}))
        self.assertEqual(text_node_to_html_node(node6), LeafNode(tag="img", value="", props={"src": "http://example.com/image.jpg", "alt": "A picture"}))
        with self.assertRaises(TypeError):
            text_node_to_html_node(node7)

if __name__ =='__main__':
    unittest.main()
