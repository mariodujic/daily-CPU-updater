import datetime
from datetime import date


class TimeUtils:
    @staticmethod
    def get_time():
        return date.today()

    def is_today(self, scheduled_time: str):
        scheduled_object = datetime.datetime.strptime(scheduled_time, "%Y-%m-%d").date()
        return scheduled_object == self.get_time()
