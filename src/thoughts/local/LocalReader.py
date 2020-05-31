import json

from src.services.Read import Read
from src.thoughts.data.Thought import Thought


class LocalReader(Read):

    def read(self):
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
                    p["used"]
                )
                thoughts.append(thought)
            return thoughts
