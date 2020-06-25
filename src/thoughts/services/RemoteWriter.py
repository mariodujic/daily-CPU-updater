from src.data.RemoteDatabase import RemoteDatabase
from src.environment.Environment import Environment
from src.services.Write import Write
from src.thoughts.data.Thought import Thought
from src.thoughts.error_handlers.LocaleError import LocaleError


class RemoteWriter(Write):

    def __init__(self, remote_database: RemoteDatabase):
        self.remote_database = remote_database

    def write(self, thought: Thought):
        print("Writing domain to firestore.")
        self.__get_doc(thought.locale.name.lower(), thought.itemId).set(thought.remote_dict())
        self.__get_reference(thought.locale.name.lower()).set(thought.remote_dict())

    def __get_doc(self, locale: str, document_id: str):
        return self.__get_collection(locale).document(document_id)

    def __get_collection(self, locale: str):
        return self.remote_database.get_firestore_client().collection(self.__get_environment_reference(locale))

    def __get_reference(self, locale: str):
        print(self.__get_environment_reference(locale))
        return self.remote_database\
            .get_database_client() \
            .reference(self.__get_environment_reference(locale)) \
            .child("latest")

    def __get_environment_reference(self, locale: str):
        if locale == "en":
            return Environment.get().THOUGHT_COLLECTION_EN
        elif locale == "hr":
            return Environment.get().THOUGHT_COLLECTION_HR
        else:
            raise LocaleError
