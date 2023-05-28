"""
Managing games.
"""


from typing import List
from .card import Card
from .deck import Deck


class Game:
    """
    Managing games.
    """

    def __init__(self, deck: Deck) -> None:
        self.deck = deck

    def deal(self) -> List[Card]:
        """
        Return List contains five cards.
        """
        hand = self.deck[:5]
        self.deck = self.deck[5:]
        return hand
