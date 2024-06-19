from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag=None, children=None, props=None):
        super().__init__(tag=tag, children=children, props=props)
        if not isinstance(self.children, list) or children is None or children == []: raise ValueError("Class requires a non-empty list of children")
        self.value = None
    def to_html(self):
        if self.tag == None: raise ValueError("Tag required")
        full_html = '' 
        full_html += ''.join(child.to_html() for child in self.children)
        return f"<{self.tag}{self.props_to_html()}>{full_html}</{self.tag}>"
