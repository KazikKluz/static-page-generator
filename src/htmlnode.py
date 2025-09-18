class HTMLNode:
    '''This class describes parent HTML node
    and its expected behaviour'''

    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        keys = list(self.props.keys())
        result = ""
        for item in keys:
            result += f' {item}="{self.props[item]}"'

        return result


class LeafNode(HTMLNode):
    def __init__(self, tag=None, value=None, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):

        if self.value is None:
            raise ValueError
        if self.tag is None:
            return self.value

        if self.props is None:

            if self.tag in ("img", "br"):
                return f"<{self.tag}/>"
            else:
                return f"<{self.tag}>{self.value}</{self.tag}>"

        else:
            if self.tag in ("img", "br"):
                return f"<{self.tag}{self.props_to_html()}/>"
            else:
                return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"


class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("Tag is mandatory in ParentNode")

        if self.children is None:
            raise ValueError("ParentNode must have children")

        return_string = ""

        for item in self.children:
            return_string += item.to_html()

        if self.props is None:
            return f"<{self.tag}>{return_string}</{self.tag}>"
        else:
            return f"<{self.tag}{self.props_to_html()}>{return_string}</{self.tag}>"
