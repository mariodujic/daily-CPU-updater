from src.services.Read import Read
from src.services.Write import Write
from src.thoughts.data.Thought import Thought
from src.utils.ListUtils import ListUtils
from src.utils.TimeUtils import TimeUtils


class ThoughtsController:
    def __init__(self, local_reader: Read, local_writer: Write, remote_writer: Write):
        self.local_reading_service = local_reader
        self.local_writing_service = local_writer
        self.remote_writing_service = remote_writer

    def write_data(self):
        if len(self.__get_today_thoughts()) == 0:
            print("There is no thought for today in JSON file")
            return
        for thought in self.__get_today_thoughts():
            self.__write_json(thought)
            self.__write_remote(thought)

    def __write_json(self, thought: Thought):
        self.local_writing_service.write(self.__thought_used_list(thought))

    def __write_remote(self, thought: Thought):
        self.remote_writing_service.write(thought)

    def __get_today_thoughts(self):
        thoughts = []
        for thought in self.__get_thoughts():
            if TimeUtils.is_today(thought.date) and not thought.used:
                thoughts.append(thought)
        return thoughts

    def __thought_used_list(self, thought: Thought):
        return ListUtils.replace_list_item(self.__get_thoughts(), thought)

    def __get_thoughts(self):
        return self.local_reading_service.read()
