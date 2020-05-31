import datetime
from datetime import date


class TimeUtils:
    @staticmethod
    def get_time():
        return date.today()

    @staticmethod
    def is_today(scheduled_time: str):
        scheduled_object = datetime.datetime.strptime(scheduled_time,
                                                      "%Y-%m-%dT%H:%M:%S.%fZ").date()
        return scheduled_object == TimeUtils.get_time()

    @staticmethod
    def current_date_and_time_as_path_stamp():
        formatted = datetime.datetime.now().strftime("%d-%m-%Y %H-%M-%S")
        return str(formatted)
