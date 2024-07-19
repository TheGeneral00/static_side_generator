import unittest
from functions import text_to_textnodes
from textnode import TextNode

class TestTextToTextNodes(unittest.TestCase):
    def test(self):
        text = "This is **text** with an *italic* word and a `code block` and an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and a [link](https://boot.dev)"

        expected_list = [
                TextNode("This is ", "text"),
                TextNode("text", "bold"),
                TextNode(" with an ", "text"),
                TextNode("italic", "italic"),
                TextNode(" word and a ", "text"),
                TextNode("code block", "code"),
                TextNode(" and an ", "text"),
                TextNode("image", "image", "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png"),
                TextNode(" and a ", "text"),
                TextNode("link", "link", "https://boot.dev")
                ]
        print(text_to_textnodes(text))
        self.assertListEqual(text_to_textnodes(text), expected_list)

if __name__ == '__main__':
    unittest.main()
