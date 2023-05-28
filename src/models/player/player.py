"""
Players model.
"""


from typing import List
from ..card import Card
from .hand import Hand


class Player:
    """
    Hand
    """

    def __init__(self, cards: List[Card]) -> None:
        self.hand = Hand(cards=cards)
