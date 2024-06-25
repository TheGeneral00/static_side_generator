import unittest
from functions import split_nodes_image, split_nodes_link
from textnode import TextNode

class TestSpliting(unittest.TestCase):
    def test_images(self):
        text = TextNode("This is text with an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and ![another](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/dfsdkjfd.png)", "text")

        expected_list = [
                TextNode("This is text with an ", "text"),
                TextNode("image", "image", "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png"),
                TextNode(" and ", "text"),
                TextNode("another", "image","https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/dfsdkjfd.png" )
                ]

        self.assertListEqual(split_nodes_image(text), expected_list)

    def test_links(self):
        text = TextNode("This is text with a [link](https://www.example.com) and [another](https://www.example.com/another)", "text")

        expected_list = [
                TextNode("This is text with a ", "text"),
                TextNode("link", "link", "https://www.example.com"),
                TextNode(" and ", "text"),
                TextNode("another", "link", "https://www.example.com/another")
                ]

        self.assertListEqual(split_nodes_link(text), expected_list)

if __name__ == '__main__':
    unittest.main()
