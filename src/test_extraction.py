import unittest
from functions import extract_markdown_images
from functions import extract_markdown_links

class TestExtraction(unittest.TestCase):
    def test_images(self):
        text = "This is text with an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and ![another](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/dfsdkjfd.png)"
        print(extract_markdown_images(text))

        expected_list = [("image", "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png"), ("another", "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/dfsdkjfd.png")]
        producedList = extract_markdown_images(text)
        self.assertListEqual(producedList, expected_list)

    def test_links(self):
        text = text = "This is text with a [link](https://www.example.com) and [another](https://www.example.com/another)"
        print(extract_markdown_links(text))

        expected_list = [("link", "https://www.example.com"), ("another", "https://www.example.com/another")]
        producedList = extract_markdown_links(text)
        self.assertListEqual(producedList, expected_list)

    def test_image_and_links(self):
        text = "This is a text with an ![image](https://example_image.net) and a [link](https://example_link.com)."
        print(extract_markdown_images(text))
        print(extract_markdown_links(text))

        expected_list_image = [("image", "https://example_image.net")]
        expected_list_link = [("link", "https://example_link.com")]
        
        producedList_images = extract_markdown_images(text)
        producedList_links = extract_markdown_links(text)
        self.assertListEqual(producedList_images, expected_list_image)
        self.assertListEqual(producedList_links, expected_list_link)

if __name__ == '__main__':
    unittest.main()
