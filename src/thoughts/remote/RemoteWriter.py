import uuid
from dataclasses import asdict

from src.services.Write import Write
from src.thoughts.data.Thought import Thought
from src.utils.ConstantUtils import CONST


class RemoteWriter(Write):

    def __init__(self, db):
        self.db = db
        self.collection = db.collection(CONST.THOUGHT_COLLECTION)
        self.doc = self.collection.document(str(uuid.uuid4()))

    def write(self, data: Thought):
        print(asdict(data))
        self.doc.set(asdict(data))
