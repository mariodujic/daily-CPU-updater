import json

from src.services.Writing import Writing
from src.thoughts.data.ThoughtEncoder import MyEncoder


class LocalWriter(Writing):
    thoughts = list()

    def write(self, thoughts: list):
        with open("assets/thoughts.json", "w") as json_file:
            json.dump(thoughts, json_file, indent=4, cls=MyEncoder)