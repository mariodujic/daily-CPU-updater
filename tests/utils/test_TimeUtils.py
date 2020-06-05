import datetime
from datetime import date
from unittest import TestCase

from src.utils.TimeUtils import TimeUtils


class TestTimeUtils(TestCase):

    def test_gets_correct_current_time(self):
        self.assertEqual(TimeUtils.get_time(), date.today())

    def test_is_date_today_asserts_false(self):
        past_time = "2020-06-03T22:00:00.000Z"
        self.assertFalse(TimeUtils.is_today(past_time))

    def test_timestamp_format_asserts_true(self):
        date_now = datetime.datetime.now()
        expected = str(date_now.strftime("%d-%m-%Y %H-%M-%S"))
        self.assertEqual(TimeUtils.current_date_and_time_as_path_stamp(), expected)
