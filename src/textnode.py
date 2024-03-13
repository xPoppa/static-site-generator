class TextNode :
    def __init__(self, text: str, text_type: str, url:str):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, value ) -> bool:
        return self.text == value.text and self.text_type == value.text_type and self.url == value.url

    def __repr__(self) -> str:
    
