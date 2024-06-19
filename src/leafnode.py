from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, tag=None, value=None, children=None, props=None):
        super().__init__(tag, value, children, props)
        if self.children != []:
            raise TypeError("Children are not allowed")
        if self.value == None:
            raise ValueError("Value is required")
        
    def to_html(self):
        if self.tag == None: return self.value
        if self.tag == "a" and self.props == {}: raise ValueError("Webadress required")
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

    def __eq__(self, other):
        return super().__eq__(other)
