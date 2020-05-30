from dataclasses import dataclass

from src.data.ItemBase import ItemBase


@dataclass
class Thought(ItemBase):
    itemId: str
    name: str
    age: int
    scheduled_at: str
    used: bool
