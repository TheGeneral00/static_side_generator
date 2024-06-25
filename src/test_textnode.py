import unittest 
from textnode import TextNode

class TestTextNode(unittest.TestCase):
    def setUp(self): 
        self.textNodes = [
            TextNode("This is a text node", "bold"),
            TextNode("This is another text node", "italic"),
            TextNode("Yet another text node", None),
            TextNode("", "bold"),
            TextNode("This is a text node", "bold"),
            ]

    def test_eq(self):
        for i in range(len(self.textNodes)):
            for j in range(i+1, len(self.textNodes)):
                node = self.textNodes[i]
                node2 = self.textNodes[j]
        
                if i == 0 and j == 4: 
                    result = (node == node2)
                    self.assertEqual(node, node2)
                else:
                    result = (node == node2)
                    self.assertNotEqual(node, node2)

               

if __name__ == "__main__":
    unittest.main()
