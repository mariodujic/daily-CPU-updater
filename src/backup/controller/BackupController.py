from src.backup.domain.BackupThoughtEncoder import BackupThoughtEncoder
from src.services.Read import Read
from src.services.Write import Write
from src.thoughts.data.Thought import Thought
from src.thoughts.data.ThoughtLocale import ThoughtLocale


class BackupController:
    def __init__(self, local_writer: Write, remote_reader: Read):
        self.local_writing_service = local_writer
        self.remote_reading_service = remote_reader

    def write_remote_data_backup(self):
        self.local_writing_service.write(
            self.__read_remote_en_data(),
            "backups/en-thoughts.json",
            BackupThoughtEncoder
        )
        self.local_writing_service.write(
            self.__read_remote_hr_data(),
            "backups/hr-thoughts.json",
            BackupThoughtEncoder
        )

    def __read_remote_en_data(self):
        thoughts = []
        for doc in self.remote_reading_service.read(ThoughtLocale.EN.name.lower()):
            thought = Thought.remote_to_object(doc.to_dict())
            thoughts.append(thought)
        return thoughts

    def __read_remote_hr_data(self):
        thoughts = []
        for doc in self.remote_reading_service.read(ThoughtLocale.HR.name.lower()):
            thought = Thought.remote_to_object(doc.to_dict())
            thoughts.append(thought)
        return thoughts
