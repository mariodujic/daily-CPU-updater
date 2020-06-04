from unittest import TestCase

from src.thoughts.data.Thought import Thought
from src.thoughts.data.ThoughtLocale import ThoughtLocale
from src.utils.ListUtils import ListUtils


class TestListUtils(TestCase):
    def setUp(self):
        self.thoughts = [
            Thought("", "", "", "a1", "", "", ThoughtLocale.EN, False),
            Thought("", "", "", "a2", "", "", ThoughtLocale.EN, False)
        ]

    def test_replaced_list_items_used_changed_true(self):
        replaced_thoughts = ListUtils.replace_list_item(self.thoughts, self.thoughts[0])
        self.assertTrue(replaced_thoughts[0].used)
        self.assertFalse(replaced_thoughts[1].used)
