from leafnode import LeafNode
from textnode import TextNode
import re

def text_node_to_html_node(text_node):
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

def split_nodes_delimiter(old_nodes, delimiter, text_type):
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
        
def extract_markdown_images(text):
    return re.findall(r"!\[(.*?)\]\((.*?)\)", text)
    
def extract_markdown_links(text):
    return re.findall(r"(?<!\!)\[(.*?)\]\((.*?)\)", text)
