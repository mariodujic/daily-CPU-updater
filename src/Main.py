from src.thoughts.controller.ThoughtsController import ThoughtsController
from src.thoughts.local.LocalReader import LocalReader
from src.thoughts.local.LocalWriter import LocalWriter
from src.thoughts.remote.Remote import Remote
from src.thoughts.remote.RemoteReader import RemoteReader


class Main:
    # dependencies
    remote = Remote()
    local_reader = LocalReader()
    local_writer = LocalWriter()
    remote_reader = RemoteReader(remote.get_client())
    thought_controller = ThoughtsController(local_reader, local_writer, remote_reader)

    def initialize(self):
        today_thought = self.thought_controller.get_today_thought()
        self.thought_controller.write_json(today_thought)
        print(self.remote_reader.read())
