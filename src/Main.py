from src.thoughts.controller.ThoughtsController import ThoughtsController
from src.thoughts.local.LocalReader import LocalReader
from src.thoughts.local.LocalWriter import LocalWriter
from src.thoughts.remote.ReadRemote import ReadRemote
from src.thoughts.remote.Remote import Remote

remote = Remote()
reading_service = LocalReader()
writing_service = LocalWriter()
print(ReadRemote(remote.get_client()).get_remote_data())
thought_controller = ThoughtsController(reading_service, writing_service)
today_thought = thought_controller.get_today_thought()
thought_controller.write_json(today_thought)
