import json

from src.services.Reading import Reading
from src.services.Writing import Writing
from src.thoughts.ReadingThoughts import ReadingThoughts
from src.thoughts.Thought import Thought
from src.thoughts.WritingThoughts import WritingThoughts
from src.utils.TimeUtils import TimeUtils


class ThoughtsController:
    reading_service: Reading = ReadingThoughts()
    writing_service: Writing = WritingThoughts()
    thoughts = reading_service.read_json()

    def get_today_thought(self):
        for thought in self.thoughts:
            if TimeUtils.is_today(thought.scheduled_at):
                return thought
        return None

    def set_today_thought_used(self, thought: Thought):
        thoughts = self.reading_service.read_json()
        thoughts.append(thought)
        self.writing_service.write_json(json.dumps(thoughts, cls=MyEncoder))


class MyEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Thought):
            return {"name": obj.name, "age": obj.age, "scheduled_at": obj.scheduled_at,
                    "used": obj.used}
        return json.JSONEncoder.default(self, obj)
