from src.services.Read import Read


class RemoteReader(Read):

    def __init__(self, db):
        self.db = db
        self.collection = db.collection("hello")

    def read(self):
        return self.collection.document("test").get()

