from src.backup.domain.BackupThoughtEncoder import BackupThoughtEncoder
from src.environment.Environment import Environment
from src.services.Read import Read
from src.services.Write import Write
from src.thoughts.data.Thought import Thought
from src.thoughts.data.ThoughtLocale import ThoughtLocale
from src.utils.TimeUtils import TimeUtils


class BackupController:
    def __init__(self, backup_writer: Write, remote_reader: Read):
        self.backup_writing_service = backup_writer
        self.remote_reading_service = remote_reader

    def write_remote_data_backup(self):
        time = TimeUtils.current_date_and_time_as_path_stamp()
        self.backup_writing_service.write(
            self.__read_remote_en_data(),
            Environment.get().LOCAL_BACKUP_PATH + "/" + time + "/",
            "en-thoughts.json",
            BackupThoughtEncoder
        )
        self.backup_writing_service.write(
            self.__read_remote_hr_data(),
            Environment.get().LOCAL_BACKUP_PATH + "/" + time + "/",
            "hr-thoughts.json",
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
