import unittest
from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def basic_test(self):
        node = LeafNode("p", "Hey ho")
        node2 = LeafNode("a", "Click Me!", props={"href": "www.example.com"})
        
        node4 = LeafNode("a", "HeyHo!", children=[LeafNode("p", "Hey ho")])
        
        self.assertEqual(node.to_html(), "<p>Hey ho</p>2")
        self.assertEqual(node2.to_html(), '<a href="www.example.com">Click me!</a>')
        
        with self.assertRaises(ValueError):
            node3 = LeafNode("p")

        with self.assertRaises(TypeError):
            node4 = LeafNode("a", "HeyHo!", children=[LeafNode("p", "Hey ho")])

    def test_eq(self):
        node = LeafNode("p", "Hey ho")
        node2 = LeafNode("p", "Hey ho")
        node3 = LeafNode("a", "Click Me!", props={"href": "www.example.com"})
        node4 = LeafNode("a", "Click Me!", props={"href": "www.example.com"})

        self.assertEqual(node, node2)
        self.assertEqual(node3, node4)
        self.assertNotEqual(node, node3)

if __name__ == '__main__':
    unittest.main()
