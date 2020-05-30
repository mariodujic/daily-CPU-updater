import json

from src.services.Writing import Writing


class WritingThoughts(Writing):
    thoughts = list()

    def write_json(self, thoughts: list):
        with open("assets/thoughts.json", "w", encoding='utf-8') as json_file:
            print(thoughts)
            json.dump(thoughts, json_file, ensure_ascii=False, indent=4)
