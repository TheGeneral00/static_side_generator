import unittest
from functions import markdown_to_html_node
from htmlnode import ParentNode
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

        expected_Node = ParentNode(tag='div',
        children=[
            ParentNode(tag='h1', children=[
                LeafNode(value='Heading 1')
                ]),
            ParentNode(tag='p',
            children=[
                LeafNode(value='This is a paragraph with some '),
                LeafNode(tag='b', value='bold text'),
                LeafNode(value=' and some '),
                LeafNode(tag='i', value='italic text'),
                LeafNode(value='. Here is a '),
                LeafNode(tag='a', value='link', props={'href': 'https://example.com'}),
                LeafNode(value='.'),
            ]),
            ParentNode(tag='blockquote', 
            children=[
                    LeafNode(value="This is a blockquote. It spans multiple lines.")
            ]),
            ParentNode(tag='ul',
            children=[
                ParentNode(tag='li', children=[
                    LeafNode(value='Item 1 in an unordered list')
                    ]),
                ParentNode(tag='li', children=[
                    LeafNode(value='Item 2 in an unordered list')
                    ]),
                ParentNode(tag='li', children=[
                        LeafNode(value='Item 3 in an unordered list with '),
                        LeafNode(tag='b', value='bold text'),
                    ])
            ]),
            ParentNode(tag='ol', 
            children=[
                ParentNode(tag='li',  children=[
                    LeafNode(value='First item in an ordered list')
                    ]),
                ParentNode(tag='li',  children=[
                    LeafNode(value='Second item in an ordered list')
                    ]),
                ParentNode(tag='li', 
                    children=[
                        LeafNode(value='Third item in an ordered list with '),
                        LeafNode(tag='i', value='italic text') 
                        ])
                    ]),
            ParentNode(tag='p', children=[
                LeafNode(value='Here is a code block:')
                ]),
            ParentNode(tag='pre', children=[
                         ParentNode(tag='code', children=[
                             LeafNode(value='def hello_world():\nprint("Hello World!")')
                             ]),
                         ]),
            ParentNode(tag='p', children=[
                         LeafNode(value='And here is more text to form another paragraph.')
                         ])
                     ])
        self.assertEqual(markdown_to_html_node(markdown), expected_Node) 
