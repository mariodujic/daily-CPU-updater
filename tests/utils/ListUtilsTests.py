from src.thoughts.data.Thought import Thought
from src.thoughts.data.ThoughtLocale import ThoughtLocale
from src.utils.ListUtils import ListUtils


def replaced_list_items_used_changed_true():
    thoughts = [
        Thought("", "", "", "a1", "", "", ThoughtLocale.EN, False),
        Thought("", "", "", "a2", "", "", ThoughtLocale.EN, False)
    ]
    replaced_thoughts = ListUtils.replace_list_item(thoughts, thoughts[0])
    assert replaced_thoughts[0].used == True, "Should be True"
    assert replaced_thoughts[1].used == False, "Should be False"


if __name__ == "__main__":
    replaced_list_items_used_changed_true()
