from src.backup.controller.BackupController import BackupController
from src.backup.services.BackupWriter import BackupWriter
from src.backup.services.RemoteReader import RemoteReader
from src.data.RemoteDatabase import RemoteDatabase
from src.thoughts.controller.ThoughtsController import ThoughtsController
from src.thoughts.services.LocalReader import LocalReader
from src.thoughts.services.LocalWriter import LocalWriter
from src.thoughts.services.RemoteWriter import RemoteWriter


class Main:
    # dependencies
    remote = RemoteDatabase()
    local_reader = LocalReader()
    local_writer = LocalWriter()
    backup_writer = BackupWriter(local_writer)
    remote_writer = RemoteWriter(remote.get_client())
    remote_reader = RemoteReader(remote.get_client())
    thought_controller = ThoughtsController(
        local_reader,
        local_writer,
        remote_writer
    )
    backup_controller = BackupController(
        backup_writer,
        remote_reader
    )

    def initialize(self):
        self.thought_controller.write_data()
        self.backup_controller.write_remote_data_backup()
