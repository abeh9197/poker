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
