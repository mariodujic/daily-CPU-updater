from src.services.Read import Read
from src.thoughts.error_handlers.LocaleError import LocaleError
from src.utils.ConstantUtils import CONST


class RemoteReader(Read):
    def __init__(self, db):
        self.db = db

    def read(self, *args):
        return self.__get_collection(*args).stream()

    def __get_collection(self, locale: str):
        if locale == "en":
            collection_str = CONST.THOUGHT_COLLECTION_EN
        elif locale == "hr":
            collection_str = CONST.THOUGHT_COLLECTION_HR
        else:
            raise LocaleError

        return self.db.collection(collection_str)
