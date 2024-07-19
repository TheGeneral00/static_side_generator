class TextNode():
    def __init__(self, text: str, text_type: str, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url
        
    def __eq__(self, TextNode):
        if self.text == TextNode.text and self.text_type == TextNode.text_type and self.url == TextNode.url:
            return True
        return False

    def __repr__(self):
        contentString = ""
        if self.text != "" and self.text !=None:
            contentString += f'"{self.text}", '
        contentString += f'"{self.text_type}"'
        if self.url != "" and self.url != None:
            contentString += f' ,"{self.url}"'
        return f"TextNode({contentString})"
