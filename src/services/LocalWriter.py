import json

from src.services.Write import Write


class LocalWriter(Write):

    def write(self, thoughts: list, path: str, encoder):
        with open(path, "w") as json_file:
            json.dump(thoughts, json_file, indent=4, cls=encoder)
