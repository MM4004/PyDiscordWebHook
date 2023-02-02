class Embed:
    def __init__(self, title: str|None = None, description: str|None = None, url: str|None = None, color: int = 0x000000):
        self.title = title
        self.description = description
        self.url = url
        self.color = color

    def modify(self, title: str|None = None, description: str|None = None, url: str|None = None, color: int = 0x000000):
        self.title = title
        self.description = description
        self.url = url
        self.color = color

    def toJSON(self):
        result = {"color": self.color,"type":"rich"}
        if isinstance(self.title, str):
            result.update({"title":self.title})
        if isinstance(self.description, str):
            result.update({"description":self.description})
        if isinstance(self.url, str):
            result.update({"url":self.url})
        return result