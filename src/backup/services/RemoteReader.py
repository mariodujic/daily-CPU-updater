from src.data.RemoteDatabase import RemoteDatabase
from src.environment.Environment import Environment
from src.services.Read import Read
from src.thoughts.error_handlers.LocaleError import LocaleError


class RemoteReader(Read):
    def __init__(self, remote_database: RemoteDatabase):
        self.remote_database = remote_database

    def read(self, *args):
        return self.__get_collection(*args).stream()

    def __get_collection(self, locale: str):
        if locale == "en":
            collection_str = Environment.get().THOUGHT_COLLECTION_EN
        elif locale == "hr":
            collection_str = Environment.get().THOUGHT_COLLECTION_HR
        else:
            raise LocaleError
        print(collection_str)
        return self.remote_database.get_firestore_client().collection(collection_str)
