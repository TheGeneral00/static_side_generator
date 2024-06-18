class TextNode():
    def __init__(self, text, text_type, url):
        self.text = text
        self.text_type = text_type
        self.url = url
    
    def __eq__(self, TextNode):
        if self.text == TextNode.text and self.text_type == TextNode.tet_type and self.url == TextNode.url:
            return True
        return False

    def __repr__(self):
        print(f"TextNode({self.text}, {self.text_type}, {self.url})")
