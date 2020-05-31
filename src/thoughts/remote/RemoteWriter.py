import uuid
from dataclasses import asdict

from src.services.Write import Write
from src.thoughts.data.Thought import Thought
from src.utils.ConstantUtils import CONST


class RemoteWriter(Write):

    def __init__(self, db):
        self.db = db
        self.collection = db.collection(CONST.THOUGHT_COLLECTION_HR)
        self.doc = self.collection.document(str(uuid.uuid4()))

    def write(self, data: Thought):
        print("Writing data to firestore.")
        self.doc.set(data.remote_dict())
