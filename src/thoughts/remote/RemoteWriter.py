import uuid

from src.services.Write import Write
from src.thoughts.data.Thought import Thought
from src.thoughts.error_handlers.LocaleError import LocaleError
from src.utils.ConstantUtils import CONST


class RemoteWriter(Write):

    def __init__(self, db):
        self.db = db

    def write(self, thought: Thought):
        print("Writing data to firestore.")
        self.__get_doc(thought.locale.name.lower()).set(thought.remote_dict())

    def __get_doc(self, locale: str):
        if locale == "en":
            collection_str = CONST.THOUGHT_COLLECTION_EN
        elif locale == "hr":
            collection_str = CONST.THOUGHT_COLLECTION_HR
        else:
            print("LOCALE ERROR")
            raise LocaleError

        collection = self.db.collection(collection_str)
        return collection.document(str(uuid.uuid4()))
