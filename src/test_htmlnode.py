from htmlnode import HTMLNode
import unittest

class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        # Identical nodes - should be equal
        node1 = HTMLNode(tag="p", value="Hello, world!")
        node2 = HTMLNode(tag="p", value="Hello, world!")
        self.assertEqual(node1, node2)
        
        # Identical nodes with props and children
        child1 = HTMLNode(tag="li", value="Item 1")
        child2 = HTMLNode(tag="li", value="Item 2")
        parent1 = HTMLNode(tag="ul", children=[child1, child2])
        parent2 = HTMLNode(tag="ul", children=[child1, child2])
        self.assertEqual(parent1, parent2)

    def test_not_eq(self):
        # Different tag
        node1 = HTMLNode(tag="p", value="Hello, world!")
        node2 = HTMLNode(tag="a", value="Hello, world!")
        self.assertNotEqual(node1, node2)

        # Different value
        node3 = HTMLNode(tag="p", value="Hello!")
        node4 = HTMLNode(tag="p", value="Hello, world!")
        self.assertNotEqual(node3, node4)

        # Different props
        node5 = HTMLNode(tag="a", value="Click here", props={"href": "https://www.example.com"})
        node6 = HTMLNode(tag="a", value="Click here", props={"target": "_blank"})
        self.assertNotEqual(node5, node6)
