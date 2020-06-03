from src.backup.domain.BackupThoughtEncoder import BackupThoughtEncoder
from src.environment.Environment import Environment
from src.services.Read import Read
from src.services.Write import Write
from src.thoughts.data.Thought import Thought
from src.thoughts.data.ThoughtLocale import ThoughtLocale
from src.utils.TimeUtils import TimeUtils
from src.view.View import View


class BackupController:
    def __init__(self, backup_writer: Write, remote_reader: Read, view: View):
        self.backup_writing_service = backup_writer
        self.remote_reading_service = remote_reader
        self.view = view

    def write_remote_data_backup(self):
        time = TimeUtils.current_date_and_time_as_path_stamp()
        thoughts_en = self.__read_remote_en_data()
        thoughts_hr = self.__read_remote_hr_data()
        self.backup_writing_service.write(
            thoughts_en,
            Environment.get().LOCAL_BACKUP_PATH + "/" + time + "/",
            "en-thoughts.json",
            BackupThoughtEncoder
        )
        self.backup_writing_service.write(
            thoughts_hr,
            Environment.get().LOCAL_BACKUP_PATH + "/" + time + "/",
            "hr-thoughts.json",
            BackupThoughtEncoder
        )
        if len(thoughts_en) > 0 and len(thoughts_hr) > 0:
            self.view.show_message(Environment.get().BACKUP_REMOTE_DATA_LOCALY_SUCCESS)
        else:
            self.view.show_message(Environment.get().BACKUP_REMOTE_DATA_LOCALLY_FAILURE)

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
