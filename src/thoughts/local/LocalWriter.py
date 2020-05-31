import json

from src.services.Write import Write
from src.thoughts.data.ThoughtEncoder import ThoughtEncoder


class LocalWriter(Write):
    thoughts = list()

    def write(self, thoughts: list):
        with open("assets/thoughts.json", "w") as json_file:
            json.dump(thoughts, json_file, indent=4, cls=ThoughtEncoder)
