from src.services.Read import Read
from src.services.Write import Write
from src.thoughts.data.Thought import Thought
from src.utils.ListUtils import ListUtils
from src.utils.TimeUtils import TimeUtils


class ThoughtsController:
    def __init__(self, read: Read, write: Write):
        self.reading_service = read
        self.writing_service = write

    def get_today_thought(self):
        for thought in self.__get_thoughts():
            if TimeUtils.is_today(thought.scheduled_at):
                return thought
        return None

    def write_json(self, thought: Thought):
        if not thought.used:
            self.writing_service.write(self.thought_used_list(thought))
        else:
            print("Today's item is already set to \"used\"")

    def thought_used_list(self, thought: Thought):
        return ListUtils.replace_list_item(self.__get_thoughts(), thought)

    def __get_thoughts(self):
        return self.reading_service.read()
