import json

from src.thoughts.data.Thought import Thought


class ThoughtEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Thought):
            return {
                "author": obj.author,
                "date": obj.date,
                "image": obj.image,
                "itemId": obj.itemId,
                "text": obj.text,
                "title": obj.title,
                "locale": obj.locale.name.lower(),
                "used": obj.used
            }
        return json.JSONEncoder.default(self, obj)
