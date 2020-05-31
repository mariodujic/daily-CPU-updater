from src.backup.controller.BackupController import BackupController
from src.backup.remote.RemoteReader import RemoteReader
from src.thoughts.controller.ThoughtsController import ThoughtsController
from src.thoughts.local.LocalReader import LocalReader
from src.thoughts.local.LocalWriter import LocalWriter
from src.thoughts.remote.Remote import Remote
from src.thoughts.remote.RemoteWriter import RemoteWriter


class Main:
    # dependencies
    remote = Remote()
    local_reader = LocalReader()
    local_writer = LocalWriter()
    remote_writer = RemoteWriter(remote.get_client())
    remote_reader = RemoteReader(remote.get_client())
    thought_controller = ThoughtsController(
        local_reader,
        local_writer,
        remote_writer
    )
    backup_controller = BackupController(
        local_writer,
        remote_reader
    )

    def initialize(self):
        self.thought_controller.write_data()
        self.backup_controller.read_remote_data()
