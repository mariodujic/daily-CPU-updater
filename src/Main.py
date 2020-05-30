from src.thoughts.controller.ThoughtsController import ThoughtsController

thought_controller = ThoughtsController()

today_thought = thought_controller.get_today_thought()
thought_controller.write_json(today_thought)
