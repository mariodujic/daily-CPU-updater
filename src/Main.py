from src.thoughts.controller.ThoughtsController import ThoughtsController
from src.thoughts.local.LocalReader import LocalReader
from src.thoughts.local.LocalWriter import LocalWriter
from src.thoughts.remote.Remote import Remote
from src.thoughts.remote.RemoteReader import RemoteReader
from src.thoughts.remote.RemoteWriter import RemoteWriter


class Main:
    # dependencies
    remote = Remote()
    local_reader = LocalReader()
    local_writer = LocalWriter()
    remote_reader = RemoteReader(remote.get_client())
    remote_writer = RemoteWriter(remote.get_client())
    thought_controller = ThoughtsController(
        local_reader,
        local_writer,
        remote_reader,
        remote_writer
    )

    def initialize(self):
        self.thought_controller.write_data()
