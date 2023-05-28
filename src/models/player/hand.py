"""
Hand class.
"""


from typing import List
from ..card import Card


class Hand:
    """
    Value is List contains Card class object.
    """

    def __init__(self, cards: List[Card]) -> None:
        self.value = cards

    def __str__(self) -> str:
        return str([card.value.value["view"] for card in self.value])

    def __getitem__(self, key):
        return self.value[key]

    def __setitem__(self, key, value):
        self.value[key] = value

    def __delitem__(self, key):
        del self.value[key]

    def __len__(self) -> str:
        return len(self.value)
