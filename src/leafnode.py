from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, tag=None, value=None, props=None):
        super().__init__(tag, value, None, props)
        if self.value == None:
            raise ValueError("Value is required")
        
    def to_html(self):
        if self.tag == None: return self.value
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

    def __eq__(self, other):
        return super().__eq__(other)

    def __repr__(self):
        contentString = ""
        if self.tag != "" and self.tag !=None:
            contentString += f'"{self.tag}", '
        contentString += f'"{self.value}"'
        if self.props != {} and self.props != None:
            contentString += f' ,"{self.props}"'
        return f"LeafNode({contentString})"
