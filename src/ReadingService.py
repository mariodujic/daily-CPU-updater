import json
from datetime import date

from src.Thought import Thought
from src.utils.TimeUtils import TimeUtils


def get_thoughts_from_json():
    thoughts = list()
    with open("assets/thoughts.json") as json_file:
        data = json.load(json_file)
    for p in data:
        thought = Thought(p["name"], p["age"], p["scheduled_at"])
        print(TimeUtils().is_today(thought.scheduled_at))
        thoughts.append(thought)
    return thoughts


