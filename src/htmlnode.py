class HtmlNode:
    def __init__(self, tag: str | None, value: str | None, children: list[str] | None, props: dict[str,str] | None) -> None:
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
       
    def to_html(self) -> None:
        raise NotImplementedError
    
    def props_to_html(self) -> str:
        if self.props:
            props = ""
            for key in self.props:
                props += f""
