import urllib.request
import json

class Message:
    def __init__(self, content: str|None = None, tts: bool = False, username: str|None = None, avatar_url: str|None = None) -> None:
        self.content = content
        self.tts = tts
        self.username = username
        self.avatar_url = avatar_url
    
    def modify(self, content: str|None = None, tts: bool = False, username: str|None = None, avatar_url: str|None = None) -> None:
        self.content = content
        self.tts = tts
        self.username = username
        self.avatar_url = avatar_url

    def toJSON(self):
        result = {"tts":self.tts}
        if isinstance(self.content, str):
            result.update({"content": self.content})
        if isinstance(self.username, str):
            result.update({"username": self.username})
        if isinstance(self.avatar_url, str):
            result.update({"avatar_url": self.avatar_url})
        return result

class DiscordHook:
    def __init__(self, id, token):
        self.id = id
        self.token = token

    def url(self) -> str:
        return "https://discord.com/api/webhooks/"+self.id+"/"+self.token

    def message(self, content: str) -> bool:
        try:
            req = urllib.request.Request(self.url(), bytes(json.dumps({"content":content}),"utf8"), method="POST")
            req.add_header("User-Agent", "Mozilla/5.0")
            req.add_header("Content-Type", "application/json")
            r = urllib.request.urlopen(req)
            if r.read() == b"":
                return True
            return False
        except:
            return False

    def send(self, msg: Message) -> bool:
        try:
            req = urllib.request.Request(self.url(), bytes(json.dumps(msg.toJSON()),"utf8"), method="POST")
            req.add_header("User-Agent", "Mozilla/5.0")
            req.add_header("Content-Type", "application/json")
            r = urllib.request.urlopen(req)
            if r.read() == b"":
                return True
            return False
        except:
            return False