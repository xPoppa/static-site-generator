from typing import Any, Mapping


class HtmlNode:
    def __init__(self, tag: str | None = None,
                 value: str | None = None,
                 children: list[Any] |  None = None,
                 props: dict[str,str | None] | None = None) -> None:
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self) -> str | None:
        raise NotImplementedError

    def props_to_html(self) -> str | None:
        if self.props == None: return ""
        props = ""
        for key in self.props:
            props += f" {key}=\"{self.props[key]}\""
        return props

    def __repr__(self) -> str:
        return f"tag: {self.tag},\n value: {self.value}, \n children: {self.children} \n props: {self.props}"

class LeafNode(HtmlNode):
    def __init__(self, tag: str | None = None, value: str | None = None, props: dict[str,str | None] | None = None) -> None:
        if value == None:
            raise ValueError("value required")
        super().__init__(tag=tag, value=value, props=props, children=None)

    def to_html(self):
        if self.tag == None:
            return self.value
        if self.props == None:
            return f"<{self.tag}>{self.value}</{self.tag}>"
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

class ParentNode(HtmlNode):
    def __init__(self, tag: str | None = None, children= None, props: dict[str, str | None] | None = None) -> None:
        if tag == None:
            raise ValueError("tag required")
        if children == None:
            raise ValueError("children required")
        super().__init__(tag=tag, children=children, props=props, value=None) 

    def to_html(self):
        if self.tag == None:
            raise ValueError("tag required")
        if self.children == None:
            raise ValueError("children required")
        html = ""
        for c in self.children:
            html += c.to_html() 
        return f"<{self.tag}{self.props_to_html()}>{html}</{self.tag}>"

