import urllib.request
import json
from pydiscordwebhook.embed import Embed as Embed

class Message:
    def __init__(self, content: str|None = None, tts: bool = False, username: str|None = None, avatar_url: str|None = None) -> None:
        self.content = content
        self.tts = tts
        self.username = username
        self.avatar_url = avatar_url
        self.embeds = [] 
    
    def modify(self, content: str|None = None, tts: bool = False, username: str|None = None, avatar_url: str|None = None) -> None:
        self.content = content
        self.tts = tts
        self.username = username
        self.avatar_url = avatar_url

    def add_embed(self, embed: Embed) -> bool:
        if len(self.embeds) > 9:
            return False
        self.embeds.append(embed)
        return True

    def toJSON(self):
        result = {"tts":self.tts}
        if isinstance(self.content, str):
            result.update({"content": self.content})
        if isinstance(self.username, str):
            result.update({"username": self.username})
        if isinstance(self.avatar_url, str):
            result.update({"avatar_url": self.avatar_url})
        if len(self.embeds) != 0:
            add = []
            for x in self.embeds:
                add.append(x.toJSON())
            result.update({"embeds": add})
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