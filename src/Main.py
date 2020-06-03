from tkinter import Tk

from src.backup.controller.BackupController import BackupController
from src.backup.services.BackupWriter import BackupWriter
from src.backup.services.RemoteReader import RemoteReader
from src.data.RemoteDatabase import RemoteDatabase
from src.environment.Environment import Environment
from src.environment.EnvironmentType import EnvironmentType
from src.thoughts.controller.ThoughtsController import ThoughtsController
from src.thoughts.services.LocalReader import LocalReader
from src.thoughts.services.LocalWriter import LocalWriter
from src.thoughts.services.RemoteWriter import RemoteWriter
from src.view.View import View


class Main:
    # dependencies
    root = Tk()
    view = View(root)
    remote = RemoteDatabase()
    local_reader = LocalReader()
    local_writer = LocalWriter()
    backup_writer = BackupWriter(local_writer)
    remote_writer = RemoteWriter(remote.get_client())
    remote_reader = RemoteReader(remote.get_client())
    thought_controller = ThoughtsController(
        local_reader,
        local_writer,
        remote_writer,
        view
    )
    backup_controller = BackupController(
        backup_writer,
        remote_reader,
        view
    )

    def initialize(self):
        # For testing purpose keep staging environment.
        # Production file "assets/thoughts.json" is in .gitignore for personal use.
        Environment.set_environment(EnvironmentType.STAGING)
        self.view.show_message(Environment.get().MESSAGE_LOADING())
        self.thought_controller.write_data()
        self.backup_controller.write_remote_data_backup()
        self.root.mainloop()
