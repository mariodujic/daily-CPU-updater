import json

from src.services.Reading import Reading
from src.thoughts.Thought import Thought


class ReadingThoughts(Reading):
    thoughts = list()

    def read_json(self):
        with open("assets/thoughts.json") as json_file:
            data = json.load(json_file)
            for p in data:
                thought = Thought(p["name"], p["age"], p["scheduled_at"])
                self.thoughts.append(thought)
            return self.thoughts
