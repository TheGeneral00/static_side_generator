from typing import Concatenate, Text
from htmlnode import ParentNode, HTMLNode
from leafnode import LeafNode
from textnode import TextNode
import re

def text_node_to_html_node(text_node: TextNode):
    if text_node.text_type == "text":
        return LeafNode(None, value=text_node.text)
    elif text_node.text_type == "bold":
        return LeafNode(tag="b", value=text_node.text)
    elif text_node.text_type == "italic":
        return LeafNode(tag="i", value=text_node.text)
    elif text_node.text_type == "code":
        return LeafNode(tag="code", value=text_node.text)
    elif text_node.text_type == "link":
        return LeafNode("a", text_node.text, {"href": text_node.url})
    elif text_node.text_type == "image":
        return LeafNode(tag="img", value="", props={"src": text_node.url, "alt": text_node.text})
    else:
        raise TypeError("The requested type is not supported")

def split_nodes_delimiter(old_nodes, delimiter, text_type) -> list[TextNode]:
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != "text":
            new_nodes.append(old_node)
            continue
        split_nodes = []
        sections = old_node.text.split(delimiter)
        if len(sections) % 2 == 0:
            raise Exception("Invalid markdown, formatted sections not closed")
        for i in range(len(sections)):
            if sections[i] == "":
                continue
            if i%2 == 0:
                split_nodes.append(TextNode(sections[i], "text"))
            else:
                split_nodes.append(TextNode(sections[i], text_type))
        new_nodes.extend(split_nodes)
    return new_nodes

        
def extract_markdown_images(text: str) -> list[tuple]:
    return re.findall(r"!\[(.*?)\]\((.*?)\)", text)
    
def extract_markdown_links(text: str) -> list[tuple]:
    return re.findall(r"(?<!\!)\[(.*?)\]\((.*?)\)", text)

def split_nodes_image(nodes) -> list[TextNode]:
    """
    Takes the text of TextNode, splits it, and creats TextNode members for found images
    :input: list of TextNode members
    :return: list of reformated TextNode members
    """
    new_nodes = []
    for old_node in nodes:
        if old_node.text_type != "text":
            new_nodes.append(old_node)
            continue
        original_text = old_node.text
        images = extract_markdown_images(original_text)
        if len(images) == 0:
            new_nodes.append(old_node)
            continue
        for image in images:
            sections = original_text.split(f"![{image[0]}]({image[1]})", 1)
            if len(sections) != 2:
                raise ValueError("Invalid markdown, image section not closed")
            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], "text"))
            new_nodes.append(
                TextNode(
                    image[0],
                    "image",
                    image[1],
                )
            )
            original_text = sections[1]
        if original_text != "":
            new_nodes.append(TextNode(original_text, "text"))
    return new_nodes


def split_nodes_link(nodes) -> list[TextNode]:
    """
    Takes the text of TextNode, splits it, and creats TextNode members for foundef text_to_textnodes(text: str)
    :input: list of TextNode members
    :return: list of reformated TextNode members
    """
    new_nodes = []
    for node in nodes:
        if node.text_type != "text":
            new_nodes.append(node)
            continue
        original_text = node.text
        links = extract_markdown_links(original_text)
        if len(links) == 0:
            new_nodes.append(node)
            continue
        while links:
            link = links.pop(0)
            sections = original_text.split(f"[{link[0]}]({link[1]})", 1)
            if len(sections) != 2:
                raise ValueError("Invalid markdown, link sections not closed")
            if sections[0]:
                new_nodes.append(TextNode(sections[0], "text"))
            new_nodes.append(TextNode(link[0], "link", link[1]))
            original_text = sections[1]
            links = extract_markdown_links(original_text)
        if original_text:
            new_nodes.append(TextNode(original_text, "text"))
    return new_nodes
    

def text_to_textnodes(text: str):
    '''
    Takes a TextNode and converts it into HTMLNode types using the split_nodes_delimiter function
    :input: TextNode
    :return: list[TextNode]
    '''
    nodes = [TextNode(text, "text")]
    nodes = split_nodes_delimiter(nodes, "**", "bold")
    nodes = split_nodes_delimiter(nodes, "*", "italic")
    nodes = split_nodes_delimiter(nodes, "`", "code")
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)
    return nodes

def markdown_to_blocks(text: str):
    '''
    Takes a markdown text and splits it into blocks
    :input: string
    :output: list[string]
    '''
    blocks = text.split("\n\n")
    new_blocks = []
    for block in blocks:
        stripped_block = block.strip(" ") 
        if stripped_block == "":
            continue
        new_blocks.append(stripped_block)
    return new_blocks

def block_to_block_type(block: str):
    '''
    Assignes a block(type: string) a block_type based on its characteristics
    :input: string
    :output: block_type
    '''
   # returns heading if block starts with '#'
    if block.startswith('#'):
        return 'heading'
    
    #returns code if block starts and ends with '```'
    elif block[:3] == '```'and block[len(block)-3:] == '```':
        return 'code'
    else:
        pattern = {'quote': r'>', 'unordered list': r'^[*-] ', 'ordered list': r'^\d+\. ' }
        if check_lines_starting_pattern(block, pattern['quote']):
            return 'quote'
        if check_lines_starting_pattern(block, pattern['unordered list']):
            return 'unordered list'
        if check_lines_starting_pattern(block, pattern['ordered list']):
            return 'ordered list'
   #return 'normal' if none of the above conditions are met
    return 'paragraph'

def check_lines_starting_pattern(block, pattern):
    '''
    Checks the startingpattern of the lines of a block
    :input: block(type: string), pattern(type: string)
    :output: True if all lines match the pattern, Flase else
    '''
    lines = block.split('\n')
    regex = re.compile(pattern)
    for line in lines:
        if not regex.match(line):
            return False
    return True

def markdown_to_html_node(markdown) -> HTMLNode:
    blocks = markdown_to_blocks(markdown)
    children = []
    for block in blocks:
        children.append(block_to_HTMLNode(block)) 
    return ParentNode('div', children)

def text_to_children(text: str) -> list[LeafNode]:
    text_nodes = text_to_textnodes(text)
    children = []
    for text_node in text_nodes:
        children.append(text_node_to_html_node(text_node))
    return children

def block_to_HTMLNode(block):
    block_type = block_to_block_type(block)
    if block_type == 'paragraph':
        return paragraph_to_html_node(block)
    if block_type == 'heading':
        return heading_to_html_node(block)
    if block_type == 'code':
        return code_to_html_node(block)
    if block_type == 'ordered list':
        return ol_to_html_node(block)
    if block_type == 'unordered list':
        return ul_to_html_node(block)
    if block_type == 'quote':
        return quote_to_html_node(block)
    raise ValueError('Invalid block type')

def paragraph_to_html_node(block) -> ParentNode:
    lines = block.split('\n')
    paragraph = ' '.join(lines)
    children = text_to_children(paragraph)
    return ParentNode("p", children)

def heading_to_html_node(block) -> ParentNode:
    counter = 0
    for char in block:
        if char == '#':
            counter += 1
        else:
            break
    if counter+1 >= len(block):
        raise ValueError(f"Invalid heading level: {counter}")
    text = block[counter+1:]
    children = text_to_children(text)
    return ParentNode(f'h{counter}', children)

def code_to_html_node(block) -> ParentNode:
    if not block.startswith('```') or not block.endswith('```'):
        raise ValueError("Invalid code block")
    text = block[3:-3]
    children = text_to_children(text)
    code = ParentNode('code', children)
    return ParentNode('pre', [ code ])

def ol_to_html_node(block) -> HTMLNode:
    items = block.split('\n')
    html_items = []
    for item in items:
        text = item[3:]
        children = text_to_children(text)
        html_items.append(ParentNode('li', children))
    return ParentNode('ol', html_items)

def ul_to_html_node(block) -> HTMLNode:
    items = block.split('\n')
    html_items = []
    for item in items:
        text = item[2:]
        children = text_to_children(text)
        html_items.append(ParentNode('li', children))
    return ParentNode('ul', html_items)

def quote_to_html_node(block) -> HTMLNode:
    lines = block.split('\n')
    new_lines = []
    for line in lines:
        if not line.startswith('> '):
            raise ValueError('Invalid quote block')
        new_lines.append(line.strip('>').strip())
    content = ' '.join(new_lines)
    children = text_to_children(content)
    return ParentNode('blockquote', children)

def extract_title(markdown):
    HTML = markdown_to_html_node(markdown)
    for child in HTML.children:
        if child.tag == 'h1':
            Leafs = child.children
            if Leafs:
                heading = ''
                for Leaf in Leafs:
                    heading += Leaf.value
                return heading
    raise Exception("No h1 heading")
