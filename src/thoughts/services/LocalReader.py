import json

from src.services.Read import Read
from src.thoughts.data.Thought import Thought


class LocalReader(Read):

    def read(self, *args):
        thoughts = list()
        with open("assets/thoughts.json") as json_file:
            thoughts_data = json.load(json_file)
            for t in thoughts_data:
                thought = Thought.json_to_object(t)
                thoughts.append(thought)
            return thoughts
