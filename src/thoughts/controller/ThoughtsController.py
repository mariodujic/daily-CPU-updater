from src.services.Read import Read
from src.services.Write import Write
from src.thoughts.data.Thought import Thought
from src.utils.ListUtils import ListUtils
from src.utils.TimeUtils import TimeUtils


class ThoughtsController:
    def __init__(self, local_reader: Read, local_writer: Write, remote_reader: Read,
                 remote_writer: Write):
        self.local_reading_service = local_reader
        self.local_writing_service = local_writer
        self.remote_reading_service = remote_reader
        self.remote_writing_service = remote_writer

    def write_data(self):
        if self.__get_today_thought() is None:
            print("There is no thought for today in JSON file")
        elif self.__get_today_thought().used:
            print("Today's item is already set to \"used\"")
        else:
            self.__write_json()
            self.__write_remote()

    def __write_json(self):
        self.local_writing_service.write(self.__thought_used_list(self.__get_today_thought()))

    def __write_remote(self):
        self.remote_writing_service.write(self.__get_today_thought())

    def __get_today_thought(self):
        for thought in self.__get_thoughts():
            if TimeUtils.is_today(thought.date):
                return thought
        return None

    def __thought_used_list(self, thought: Thought):
        return ListUtils.replace_list_item(self.__get_thoughts(), thought)

    def __get_thoughts(self):
        return self.local_reading_service.read()
