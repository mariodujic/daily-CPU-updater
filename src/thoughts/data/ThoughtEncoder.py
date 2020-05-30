import json

from src.thoughts.data.Thought import Thought


class MyEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Thought):
            return {
                "itemId": obj.itemId,
                "name": obj.name,
                "age": obj.age,
                "scheduled_at": obj.scheduled_at,
                "used": obj.used
            }
        return json.JSONEncoder.default(self, obj)
