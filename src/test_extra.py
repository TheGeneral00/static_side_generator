import unittest
from functions import split_nodes_delimiter, split_nodes_link, text_node_to_html_node
from leafnode import LeafNode
from textnode import TextNode

class TestExtra(unittest.TestCase):

   def test(self):
        node = TextNode("**I like Tolkien**. Read my [first post here](/majesty) (sorry the link doesn't work yet)", 'text')
        result = split_nodes_delimiter([node], '**', 'bold')
        result = split_nodes_link(result)
        expected = [
                TextNode('I like Tolkien', 'bold'),
                TextNode('. Read my ', 'text'),
                TextNode('first post here', 'link', '/majesty'),
                TextNode(" (sorry the link doesn't work yet)", 'text')
                ]
        self.assertEqual(result, expected)
        result_html = []
        for node in result:
            result_html.append(text_node_to_html_node(node))
        expected_html = [
                LeafNode('b', 'I like Tolkien'),
                LeafNode(None, '. Read my '),
                LeafNode('a', 'first post here', {'href': '/majesty'}),
                LeafNode(None, " (sorry the link doesn't work yet)")
                ]
        self.assertListEqual(result_html, expected_html)

if __name__=="__main__":
   unittest.main() 
