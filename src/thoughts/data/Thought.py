from dataclasses import dataclass


@dataclass
class Thought:
    author: str
    date: str  # 2020-04-27T22:00:00.000Z
    image: str
    itemId: str
    text: str
    title: str
    used: bool

    def remote_dict(self):
        return {
            "author": self.author,
            "date": self.date,
            "image": self.image,
            "itemId": self.itemId,
            "text": self.text,
            "title": self.title,
        }
