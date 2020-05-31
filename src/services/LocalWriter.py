import json

from src.services.Write import Write
from src.thoughts.data.ThoughtEncoder import ThoughtEncoder


class LocalWriter(Write):

    def write(self, thoughts: list, path: str):
        with open(path, "w") as json_file:
            json.dump(thoughts, json_file, indent=4, cls=ThoughtEncoder)
