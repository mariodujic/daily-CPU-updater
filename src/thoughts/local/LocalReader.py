import json

from src.services.Read import Read
from src.thoughts.data.Thought import Thought
from src.thoughts.data.ThoughtLocale import ThoughtLocale


class LocalReader(Read):

    def read(self, *args):
        thoughts = list()
        with open("assets/thoughts.json") as json_file:
            data = json.load(json_file)
            for p in data:
                thought = Thought(
                    p["author"],
                    p["date"],
                    p["image"],
                    p["itemId"],
                    p["text"],
                    p["title"],
                    ThoughtLocale(p["locale"]),
                    p["used"]
                )
                thoughts.append(thought)
            return thoughts
