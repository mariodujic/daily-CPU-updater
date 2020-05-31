from src.services.Read import Read
from src.services.Write import Write


class BackupController:
    def __init__(self, local_writer: Write, remote_reader: Read):
        self.local_writing_service = local_writer
        self.remote_reading_service = remote_reader

    def read_remote_data(self):
        for doc in self.remote_reading_service.read("en"):
            print(u'{}'.format(doc.to_dict()))
