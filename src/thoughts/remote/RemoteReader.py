from src.services.Read import Read


class RemoteReader(Read):

    def __init__(self, db):
        self.db = db
        self.collection = db.collection("hello")
        self.doc = self.collection.document("test")

    def read(self):
        if self.doc.exists:
            return format(self.doc.to_dict())
        else:
            return None

