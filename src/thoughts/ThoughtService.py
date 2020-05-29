from src.services.Reading import Reading
from src.thoughts.ReadingThoughts import ReadingThoughts
from src.utils.TimeUtils import TimeUtils


class ThoughtService:
    service: Reading = ReadingThoughts()

    def get_today_thought(self):
        thoughts = self.service.read_json()
        for thought in thoughts:
            if TimeUtils.is_today(thought.scheduled_at):
                return thought
        return None
