import datetime
from datetime import date

from src.utils.TimeUtils import TimeUtils


def gets_correct_current_time():
    assert TimeUtils.get_time() == date.today(), "Should be True"


def is_date_today_asserts_false():
    past_time = "2020-06-03T22:00:00.000Z"
    assert TimeUtils.is_today(past_time) == False, "Should be False"


def timestamp_format_asserts_true():
    date_now = datetime.datetime.now()
    expected = str(date_now.strftime("%d-%m-%Y %H-%M-%S"))
    assert TimeUtils.current_date_and_time_as_path_stamp() == expected, "Should be True"


if __name__ == "__main__":
    gets_correct_current_time()
    is_date_today_asserts_false()
    timestamp_format_asserts_true()
