from src.services.Read import Read
from src.services.Write import Write
from src.thoughts.data.Thought import Thought
from src.utils.ListUtils import ListUtils
from src.utils.TimeUtils import TimeUtils


class ThoughtsController:
    def __init__(self, local_reader: Read, local_writer: Write, remote_reader: Read):
        self.local_reading_service = local_reader
        self.local_writing_service = local_writer
        self.remote_reading_service = remote_reader

    def get_today_thought(self):
        for thought in self.__get_thoughts():
            if TimeUtils.is_today(thought.scheduled_at):
                return thought
        return None

    def write_json(self, thought: Thought):
        if not thought.used:
            self.local_writing_service.write(self.thought_used_list(thought))
        else:
            print("Today's item is already set to \"used\"")

    def thought_used_list(self, thought: Thought):
        return ListUtils.replace_list_item(self.__get_thoughts(), thought)

    def __get_thoughts(self):
        return self.local_reading_service.read()
