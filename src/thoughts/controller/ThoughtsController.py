from src.environment.Environment import Environment
from src.services.Read import Read
from src.services.Write import Write
from src.thoughts.data.ExtendedThoughtEncoder import ExtendedThoughtEncoder
from src.thoughts.data.Thought import Thought
from src.utils.ListUtils import ListUtils
from src.utils.TimeUtils import TimeUtils
from src.view.View import View


class ThoughtsController:
    def __init__(self, local_reader: Read, local_writer: Write, remote_writer: Write, view: View):
        self.local_reading_service = local_reader
        self.local_writing_service = local_writer
        self.remote_writing_service = remote_writer
        self.view = view

    def write_data(self):
        if len(self.__get_today_thoughts()) == 0:
            self.view.show_message(Environment.get().WRITE_REMOTE_DATA_FAILURE)
            return
        thoughts = self.__get_today_thoughts()
        for thought in thoughts:
            self.__write_json(thought)
            self.__write_remote(thought)
        self.view.show_message("{}{}".format(Environment.get().WRITE_REMOTE_DATA_SUCCESS, len(thoughts)))

    def __write_json(self, thought: Thought):
        self.local_writing_service.write(
            self.__thought_used_list(thought),
            Environment.get().LOCAL_THOUGHT_PATH,
            ExtendedThoughtEncoder
        )

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
