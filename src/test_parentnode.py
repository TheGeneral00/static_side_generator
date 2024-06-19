from parentnode import ParentNode
from leafnode import LeafNode
import unittest

class TestParentNode(unittest.TestCase):

    def test_constructor_errors(self):
        with self.assertRaises(ValueError):
            ParentNode("div", None)
        
        with self.assertRaises(ValueError):
            ParentNode("div", [])
    
    def test_simple_html(self):
        node = ParentNode("p", [LeafNode("b", "Hello World!")])
        self.assertEqual(node.to_html(), "<p><b>Hello World!</b></p>")
    
    def test_nested_html(self):
        node1 = ParentNode("p", [LeafNode("b", "Bold text"), LeafNode(None, "Normal text")])
        node2 = ParentNode("p", [LeafNode("i", "italic text"), LeafNode(None, "Normal text")])
        parent_node = ParentNode("div", [node1, node2])
        expected_html = "<div><p><b>Bold text</b>Normal text</p><p><i>italic text</i>Normal text</p></div>"
        self.assertEqual(parent_node.to_html(), expected_html)
    
    def test_html_with_attributes(self):
        node = ParentNode("a", [LeafNode(None, "Link text")], props={"href": "www.example.com"})
        self.assertEqual(node.to_html(), '<a href="www.example.com">Link text</a>')

if __name__ == '__main__':
    unittest.main()
