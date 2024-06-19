class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children if children is not None else []
        self.props = props if props is not None else {}

    def to_html(self):
        raise NotImplementedError()

    def props_to_html(self):
        if isinstance(self.props, dict):
            full_html = ""
            for key, value in self.props.items():
                full_html += f' {key}="{value}"'
            return full_html
        else: raise ValueError("Props is not a dictionary")

    def __repr__(self):
        return f"HTMLNode(tag='{self.tag}', value='{self.value}', children={self.children}, props={self.props})"

    def __eq__(self, other):
        if isinstance(other, HTMLNode): 
            return (self.tag == other.tag and
                    self.value == other.value and
                    self.children == other.children and
                    self.props == other.props)
        else: return False
