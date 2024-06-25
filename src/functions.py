from leafnode import LeafNode
from textnode import TextNode
import re

def text_node_to_html_node(text_node: TextNode):
    if text_node.text_type == "text":
        return LeafNode(value=text_node.text)
    elif text_node.text_type == "bold":
        return LeafNode(tag="b", value=text_node.text)
    elif text_node.text_type == "italic":
        return LeafNode(tag="i", value=text_node.text)
    elif text_node.text_type == "code":
        return LeafNode(tag="code", value=text_node.text)
    elif text_node.text_type == "link":
        return LeafNode(tag="a", value=text_node.text, props={"href": text_node.url})
    elif text_node.text_type == "image":
        return LeafNode(tag="img", value="", props={"src": text_node.url, "alt": text_node.text})
    else:
        raise TypeError("The requested type is not supported")

def split_nodes_delimiter(old_nodes, delimiter: str, text_type: str):
    new_nodes = []
    delimiter_to_text_type = {"**": "bold", "*": "italic", "`": "code"}
    
    #iterating through old_nodes
    for node in old_nodes:
        #checking if node is of TextNode class
        if not isinstance(node, TextNode) or node.text_type != "text":
            new_nodes.append(node)
            
        #spliting and iterating through node splits
        else:
            #checking for validity of text_type
            if text_type not in delimiter_to_text_type.values():
                raise ValueError("Text type/delimiter is not supported")
            
            #checking if delimiter matches text_type
            if delimiter_to_text_type[delimiter] != text_type:
                raise ValueError("Delimiter and text type aren't matching") 
             
            splitNode = []
            sections = node.text.split(delimiter)
            
            if len(sections)%2 == 0:
                raise ValueError("invalid markdown, formated section not closed")
            
            for i in range(len(sections)):
                if sections[i] == "":
                    continue
                if i % 2 == 0:
                    splitNode.append(TextNode(sections[i], "text"))
                else: splitNode.append(TextNode(sections[i], text_type))
            new_nodes.extend(splitNode)
    return new_nodes
        
def extract_markdown_images(text: str):
    return re.findall(r"!\[(.*?)\]\((.*?)\)", text)
    
def extract_markdown_links(text: str):
    return re.findall(r"(?<!\!)\[(.*?)\]\((.*?)\)", text)

def split_nodes_image(nodes):
    """
    Takes the text of TextNode, splits it, and creats TextNode members for found images
    :input: list of TextNode members
    :return: list of reformated TextNode members
    """
    new_nodes = []
    if isinstance(nodes, list):    
        for node in nodes:
            images = extract_markdown_images(node.text)
            if images == []:
                new_nodes.append(node)
            
            for image in images:
                splits = node.text.split(f"![{image[0]}]({image[1]})")
                node.text = splits[1]
                if splits[0] != "":    
                    new_nodes.append(TextNode(splits[0], "text"))
                new_nodes.append(TextNode(image[0], "image", image[1]))
    else:
        images = extract_markdown_images(nodes.text)
        if images == []:
            new_nodes.append(nodes)
            
        for image in images:
            splits = nodes.text.split(f"![{image[0]}]({image[1]})")
            nodes.text = splits[1]
            if splits[0] != "":    
                new_nodes.append(TextNode(splits[0], "text"))
            new_nodes.append(TextNode(image[0], "image", image[1]))
    return new_nodes


def split_nodes_link(nodes):
    """
    Takes the text of TextNode, splits it, and creats TextNode members for found links
    :input: list of TextNode members
    :return: list of reformated TextNode members
    """
    new_nodes = []
    if isinstance(nodes, list):    
        for node in nodes:
            links = extract_markdown_links(node.text)
            if links == []:
                new_nodes.append(node)
            
            for link in links:
                splits = node.text.split(f"[{link[0]}]({link[1]})")
                node.text = splits[1]
                if splits[0] != "":    
                    new_nodes.append(TextNode(splits[0], "text"))
                new_nodes.append(TextNode(link[0], "link", link[1]))
    else:
        links = extract_markdown_links(nodes.text)
        if links == []:
            new_nodes.append(nodes)
            
        for link in links:
            splits = nodes.text.split(f"[{link[0]}]({link[1]})")
            nodes.text = splits[1]
            if splits[0] != "":    
                new_nodes.append(TextNode(splits[0], "text"))
            new_nodes.append(TextNode(link[0], "link", link[1]))
    return new_nodes


