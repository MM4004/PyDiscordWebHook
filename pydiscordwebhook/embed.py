class EmbedFooter:
    def __init__(self, text: str|None = None, icon_url: str|None = None, proxy_icon_url: str|None = None):
        self.text = text
        self.icon_url = icon_url
        self.proxy_icon_url = proxy_icon_url

    def modify(self, text: str|None = None, icon_url: str|None = None, proxy_icon_url: str|None = None):
        if isinstance(text, str):
            self.text = text
        if isinstance(icon_url, str):
            self.icon_url = icon_url
        if isinstance(proxy_icon_url, str):
            self.proxy_icon_url = proxy_icon_url

    def toJSON(self):
        result = {}
        if self.text != None:
            result.update({"text":self.text});
        if self.proxy_icon_url != None:
            result.update({"proxy_icon_url":self.proxy_icon_url});
        if self.icon_url != None:
            result.update({"icon_url":self.icon_url});
        return result

class Embed:
    def __init__(self, title: str|None = None, description: str|None = None, url: str|None = None, color: int = 0x000000):
        self.title = title
        self.description = description
        self.url = url
        self.color = color
        self.footer = None

    def setfooter(self, value: EmbedFooter):
        self.footer = value

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
        if self.footer != None:
            result.update({"footer":self.footer.toJSON()})
        return result