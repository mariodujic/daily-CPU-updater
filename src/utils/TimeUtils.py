import datetime
from datetime import date


class TimeUtils:
    @staticmethod
    def get_time():
        return date.today()

    @staticmethod
    def is_today(scheduled_time: str):
        scheduled_object = datetime.datetime.strptime(scheduled_time, "%Y-%m-%d").date()
        return scheduled_object == TimeUtils.get_time()
