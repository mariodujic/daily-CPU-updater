from dataclasses import dataclass


@dataclass
class Thought:
    itemId: str
    name: str
    age: int
    scheduled_at: str
    used: bool
