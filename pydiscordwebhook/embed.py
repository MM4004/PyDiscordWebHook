class EmbedFooter:
    def __init__(self, text: str|None = None, icon_url: str|None = None, proxy_icon_url: str|None = None):
        if text != None:
            if len(text) > 2048:
                raise ValueError("Invalid string size")
        self.text = text
        self.icon_url = icon_url
        self.proxy_icon_url = proxy_icon_url

    def modify(self, text: str|None = None, icon_url: str|None = None, proxy_icon_url: str|None = None):
        if text != None:
            if len(text) > 2048:
                raise ValueError("Invalid string size")
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
    
class EmbedAuthor:
    def __init__(self, name: str, url:str|None = None, icon_url:str|None = None, proxy_icon_url:str|None = None):
        if name != None:
            if len(name) > 256:
                raise ValueError("Invalid string size")
        self.name = name
        self.url = url
        self.icon_url = icon_url
        self.proxy_icon_url = proxy_icon_url
    
    def modify(self, name: str|None = None, url:str|None = None, icon_url:str|None = None, proxy_icon_url:str|None = None):
        if name != None:
            if len(name) > 256:
                raise ValueError("Invalid string size")
        if name != None:
            self.name = name
        if url != None:
            self.url = url
        if icon_url != None:
            self.icon_url = icon_url
        if proxy_icon_url != None:
            self.proxy_icon_url = proxy_icon_url

    def toJSON(self):
        result = {}
        if self.name != None:
            result.update({"name":self.name})
        if self.url != None:
            result.update({"url":self.url})
        if self.icon_url != None:
            result.update({"icon_url":self.icon_url})
        if self.proxy_icon_url != None:
            result.update({"proxy_icon_url":self.proxy_icon_url})
        return result

class EmbedImage:
    def __init__(self, url:str, proxy_url:str|None = None, height:int|None = None, width:int|None = None):
        if width != None:
            if width <= 0:
                raise ValueError("Width cannot be negative")
        if height != None:
            if height <= 0:
                raise ValueError("Height cannot be negative")
        self.url = url
        self.proxy_url = proxy_url
        self.height = height
        self.width = width

    def modify(self, url:str|None = None, proxy_url:str|None = None, height:int|None = None, width:int|None = None):
        if width != None:
            if width <= 0:
                raise ValueError("Width cannot be negative")
            else:
                self.width = width
        if height != None:
            if height <= 0:
                raise ValueError("Height cannot be negative")
            else:
                self.height = height
        if url != None:
            self.url = url
        if proxy_url != None:
            self.proxy_url = proxy_url

    def toJSON(self):
        result = {}
        if self.height != None:
            result.update({"height":self.height})
        if self.width != None:
            result.update({"width":self.width})
        if self.url != None:
            result.update({"url":self.url})
        if self.proxy_url != None:
            result.update({"proxy_url":self.proxy_url})
        return result

class Embed:
    def __init__(self, title: str|None = None, description: str|None = None, url: str|None = None, color: int = 0x000000, image:EmbedImage|None = None, author:EmbedAuthor|None = None):
        if(title != None):
            if len(title) > 256:
                raise ValueError("Invalid string size")
        if(description != None):
            if len(description) > 4096:
                raise ValueError("Invalid string size")
        self.title = title
        self.description = description
        self.url = url
        self.color = color
        self.footer = None
        self.image = image
        self.author = author

    def setfooter(self, value: EmbedFooter):
        self.footer = value

    def modify(self, title: str|None = None, description: str|None = None, url: str|None = None, color: int|None = None, image:EmbedImage|None = None, author:EmbedAuthor|None = None):
        if(title != None):
            if len(title) > 256:
                raise ValueError("Invalid string size")
        if(description != None):
            if len(description) > 4096:
                raise ValueError("Invalid string size")
        if title != None:
            self.title = title
        if description != None:
            self.description = description
        if url != None:
            self.url = url
        if color != None:
            self.color = color
        if image != None:
            self.image = image
        if author != None:
            self.author = author

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
        if self.image != None:
            result.update({"image":self.image.toJSON()})
        if self.author != None:
            result.update({"author":self.author.toJSON()})
        return result