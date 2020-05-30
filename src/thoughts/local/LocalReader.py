import json

from src.services.Read import Read
from src.thoughts.data.Thought import Thought


class LocalReader(Read):

    def read(self):
        thoughts = list()
        with open("assets/thoughts.json") as json_file:
            data = json.load(json_file)
            for p in data:
                thought = Thought(p["itemId"], p["name"], p["age"], p["scheduled_at"], p["used"])
                thoughts.append(thought)
            json_file.close()
            return thoughts
