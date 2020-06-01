import uuid

from src.environment.Environment import Environment
from src.services.Write import Write
from src.thoughts.data.Thought import Thought
from src.thoughts.error_handlers.LocaleError import LocaleError


class RemoteWriter(Write):

    def __init__(self, db):
        self.db = db

    def write(self, thought: Thought):
        print("Writing domain to firestore.")
        self.__get_doc(thought.locale.name.lower()).set(thought.remote_dict())

    def __get_doc(self, locale: str):
        return self.__get_collection(locale).document(str(uuid.uuid4()))

    def __get_collection(self, locale: str):
        if locale == "en":
            collection_str = Environment.get().THOUGHT_COLLECTION_EN
        elif locale == "hr":
            collection_str = Environment.get().THOUGHT_COLLECTION_HR
        else:
            raise LocaleError

        return self.db.collection(collection_str)
