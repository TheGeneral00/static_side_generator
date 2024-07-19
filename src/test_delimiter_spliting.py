import unittest
from textnode import TextNode
from functions import split_nodes_delimiter

class TestSplitNodesDelimiter(unittest.TestCase):
    
    def test_bold_text(self):
        node = TextNode("This is a **bold** text", "text")
        result = split_nodes_delimiter([ node ], "**", "bold")
        expected = [
            TextNode("This is a ", "text"),
            TextNode("bold", "bold"),
            TextNode(" text", "text")
        ]
        self.assertEqual(result, expected)

    def test_italic_text(self):
        node = TextNode("This is an *italic* text", "text")
        result = split_nodes_delimiter([ node ], "*", "italic")
        expected = [
            TextNode("This is an ", "text"),
            TextNode("italic", "italic"),
            TextNode(" text", "text")
        ]
        self.assertEqual(result, expected)

    def test_code_text(self):
        node = TextNode("This is a `code` text", "text")
        result = split_nodes_delimiter([ node ], "`", "code")
        expected = [
            TextNode("This is a ", "text"),
            TextNode("code", "code"),
            TextNode(" text", "text")
        ]
        self.assertEqual(result, expected)
        
    def test_multiple_types(self):
        node = TextNode("This is a **bold** and *italic* text with `code`", "text")
        result = split_nodes_delimiter([ node ], "**", "bold")
        result = split_nodes_delimiter(result, "*", "italic")
        result = split_nodes_delimiter(result, "`", "code")
        expected = [
            TextNode("This is a ", "text"),
            TextNode("bold", "bold"),
            TextNode(" and ", "text"),
            TextNode("italic", "italic"),
            TextNode(" text with ", "text"),
            TextNode("code", "code")
        ]
        self.assertEqual(result, expected)
    
if __name__ == '__main__':
    unittest.main() 
