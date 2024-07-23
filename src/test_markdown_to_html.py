import unittest
from functions import markdown_to_html_node
from htmlnode import HTMLNode
from textnode import TextNode
from leafnode import LeafNode

class TestMarkdownToHTML(unittest.TestCase):

    def test(self):
        markdown = """# Heading 1

This is a paragraph with some **bold text** and some *italic text*. Here is a [link](https://example.com).

> This is a blockquote.
> It spans multiple lines.

- Item 1 in an unordered list
- Item 2 in an unordered list
- Item 3 in an unordered list with **bold text**

1. First item in an ordered list
2. Second item in an ordered list
3. Third item in an ordered list with *italic text*

Here is a code block:

```def hello_world():
print("Hello World!")```

And here is more text to form another paragraph."""

        expected_Node = HTMLNode(tag='div', value=None,
        children=[
            HTMLNode(tag='h1', value=None, children=[
                LeafNode(value='Heading 1')
                ]),
            HTMLNode(tag='p', value=None,
            children=[
                LeafNode(value='This is a paragraph with some '),
                LeafNode(tag='b', value='bold text'),
                LeafNode(value=' and some '),
                LeafNode(tag='i', value='italic text'),
                LeafNode(value='. Here is a '),
                LeafNode(tag='a', value='link', props={'href': 'https://example.com'}),
                LeafNode(value='.'),
            ]),
            HTMLNode(tag='blockquote', value=None,
            children=[
                    LeafNode(value="This is a blockquote. It spans multiple lines.")
            ]),
            HTMLNode(tag='ul', value=None,
            children=[
                HTMLNode(tag='li', value=None, children=[
                    LeafNode(value='Item 1 in an unordered list')
                    ]),
                HTMLNode(tag='li', value=None, children=[
                    LeafNode(value='Item 2 in an unordered list')
                    ]),
                HTMLNode(tag='li', value=None,
                    children=[
                        LeafNode(value='Item 3 in an unordered list with '),
                        LeafNode(tag='b', value='bold text'),
                    ])
            ]),
            HTMLNode(tag='ol', value=None,
            children=[
                HTMLNode(tag='li', value=None, children=[
                    LeafNode(value='First item in an ordered list')
                    ]),
                HTMLNode(tag='li', value=None, children=[
                    LeafNode(value='Second item in an ordered list')
                    ]),
                HTMLNode(tag='li', value=None,
                    children=[
                        LeafNode(value='Third item in an ordered list with '),
                        LeafNode(tag='i', value='italic text') 
                        ])
                    ]),
            HTMLNode(tag='p', value=None, children=[
                LeafNode(value='Here is a code block:')
                ]),
            HTMLNode(tag='pre', value=None, 
                     children=[
                         HTMLNode(tag='code', value=None, children=[
                             LeafNode(value='def hello_world():\nprint("Hello World!")')
                             
                             ]),
                         ]),
            HTMLNode(tag='p', value=None, 
                     children=[
                         LeafNode(value='And here is more text to form another paragraph.')
                         ])
                     ])
        self.assertEqual(markdown_to_html_node(markdown), expected_Node) 
