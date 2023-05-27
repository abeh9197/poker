"""
Deck
"""
from __future__ import annotations
import random

from typing import List
from .card import Card


class Deck:
    """
    Deck
    """
    def __init__(self) -> None:
        self.__value = self.__initialize()
        self.value = self.__value

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

    def __initialize(self) -> List[Card]:
        """
        Called when Deck class instance was initialized.
        Return List which have 52 Card class object.
        """
        return [Card.from_number(number) for number in range(52)]
    
    def shuffle(self) -> None:
        """
        Shuffle own value.
        """
        random.shuffle(self.value)
