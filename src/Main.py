from src.thoughts.ThoughtsController import ThoughtsController

thought_service = ThoughtsController()

thought_service.set_today_thought_used(thought_service.get_today_thought())
