from src.services.Reading import Reading
from src.services.Writing import Writing
from src.thoughts.data.Thought import Thought
from src.thoughts.services.ReadingThoughts import ReadingThoughts
from src.thoughts.services.WritingThoughts import WritingThoughts
from src.utils.ListUtils import ListUtils
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

    def write_json(self, thought: Thought):
        if not thought.used:
            self.writing_service.write_json(self.thought_used_list(thought))
        else:
            print("Today's item is already set to \"used\"")

    def thought_used_list(self, thought: Thought):
        print(len(self.thoughts))
        return ListUtils.replace_list_item(self.thoughts, thought)
