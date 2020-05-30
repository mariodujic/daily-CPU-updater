from src.thoughts.controller.ThoughtsController import ThoughtsController
from src.thoughts.local.LocalReader import LocalReader
from src.thoughts.local.LocalWriter import LocalWriter
from src.thoughts.remote.Remote import Remote
from src.thoughts.remote.RemoteReader import RemoteReader


class Main:
    # dependencies
    remote = Remote()
    read_service = LocalReader()
    write_service = LocalWriter()
    thought_controller = ThoughtsController(read_service, write_service)

    def initialize(self):
        today_thought = self.thought_controller.get_today_thought()
        self.thought_controller.write_json(today_thought)
        print(RemoteReader(self.remote.get_client()).get_remote_data())
