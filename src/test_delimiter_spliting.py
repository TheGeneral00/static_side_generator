import unittest
from functions import split_nodes_delimiter
from leafnode import LeafNode
from textnode import TextNode

class TestDelimiterSplitting(unittest.TestCase):
    def node_list_equal(self, node1, node2):
        i = 0
        while i< len(node1):
            if type(node1[i]) == TextNode: 
                if type(node1[i]) != type(node2[i]) or node1[i].text != node2[i].text or node1[i].text_type != node2[i].text_type:
                    print(node1[i], node2[i])
                    return False
            else:
                if type(node1[i]) != type(node2[i]):
                    return False
            i += 1
        return True
    
    def test(self):
        old_nodes= [
                TextNode("This is normal text", "text"),
                TextNode("This is a **bold** text", "bold"),
                TextNode("This is *italic* text", "italic"),
                TextNode("This is an `code block` text", "text"),
                TextNode("This is an #image", "image"),
                LeafNode("p", "This is a LeafNode"), 
                TextNode("This one got wrong delimiters for **italic** text", "bold")
                ]

        # Run function to be tested
        new_nodes_bold = split_nodes_delimiter(old_nodes, "**", "bold")
        
        new_nodes_italic = split_nodes_delimiter(old_nodes, "*", "italic")
        new_nodes_code = split_nodes_delimiter(old_nodes, "`", "code")
               # Define expected results
        expected_bold = [
            TextNode("This is normal text", "text"),
            TextNode("This is a ", "text"),
            TextNode("bold", "bold"),
            TextNode(" text", "text"),
            TextNode("This is *italic* text", "text"),
            TextNode("This is an `code block` text", "text"),
            TextNode("This is an #image", "text"),
            LeafNode("p", "This is a LeafNode"),
            TextNode("This one got wrong delimiters for ", "text"),
            TextNode("italic", "bold"),
            TextNode(" text", "text"),
        ]

        expected_italic = [
            TextNode("This is normal text", "text"),
            TextNode("This is a **bold** text", "text"),
            TextNode("This is ", "text"),
            TextNode("italic", "italic"),
            TextNode(" text", "text"),
            TextNode("This is an `code block` text", "text"),
            TextNode("This is an #image", "image"),
            LeafNode("p", "This is a LeafNode"),
            TextNode("This one got wrong delimiters for **italic** text", "text")
            ]

        expected_code = [
            TextNode("This is normal text", "text"),
            TextNode("This is a **bold** text", "text"),
            TextNode("This is *italic* text", "text"),
            TextNode("This is an ", "text"),
            TextNode("code block", "code"),
            TextNode(" text", "text"),
            TextNode("This is an #image", "image"),
            LeafNode("p", "This is a LeafNode"), 
            TextNode("This one got wrong delimiters for **italic** text", "text")
            ]
        
        self.assertTrue(self.node_list_equal(new_nodes_bold, expected_bold))
        self.assertTrue(self.node_list_equal(new_nodes_italic, expected_italic))
        self.assertTrue(self.node_list_equal(new_nodes_code, expected_code))

if __name__ == '__main__':
    unittest.main()

