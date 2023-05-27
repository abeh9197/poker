"""
Card Models.
"""
from __future__ import annotations


from enum import Enum


class CardValue(Enum):
    """
    Card values.
    """
    ACE_PIKES = {"id_": 0, "view": "♠A", "suit": "PIKES", "number": 1}
    TWO_PIKES = {"id_": 1, "view": "♠2", "suit": "PIKES", "number": 2}
    THREE_PIKES = {"id_": 2, "view": "♠3", "suit": "PIKES", "number": 3}
    FOUR_PIKES = {"id_": 3, "view": "♠4", "suit": "PIKES", "number": 4}
    FIVE_PIKES = {"id_": 4, "view": "♠5", "suit": "PIKES", "number": 5}
    SIX_PIKES = {"id_": 5, "view": "♠6", "suit": "PIKES", "number": 6}
    SEVEN_PIKES = {"id_": 6, "view": "♠7", "suit": "PIKES", "number": 7}
    EIGHT_PIKES = {"id_": 7, "view": "♠8", "suit": "PIKES", "number": 8}
    NINE_PIKES = {"id_": 8, "view": "♠9", "suit": "PIKES", "number": 9}
    TEN_PIKES = {"id_": 9, "view": "♠10", "suit": "PIKES", "number": 10}
    JACK_PIKES = {"id_": 10, "view": "♠11", "suit": "PIKES", "number": 11}
    QUEEN_PIKES = {"id_": 11, "view": "♠12", "suit": "PIKES", "number": 12}
    KING_PIKES = {"id_": 12, "view": "♠13", "suit": "PIKES", "number": 13}
    ACE_HEARTS = {"id_": 13, "view": "♥A", "suit": "HEARTS", "number": 1}
    TWO_HEARTS = {"id_": 14, "view": "♥2", "suit": "HEARTS", "number": 2}
    THREE_HEARTS = {"id_": 15, "view": "♥3", "suit": "HEARTS", "number": 3}
    FOUR_HEARTS = {"id_": 16, "view": "♥4", "suit": "HEARTS", "number": 4}
    FIVE_HEARTS = {"id_": 17, "view": "♥5", "suit": "HEARTS", "number": 5}
    SIX_HEARTS = {"id_": 18, "view": "♥6", "suit": "HEARTS", "number": 6}
    SEVEN_HEARTS = {"id_": 19, "view": "♥7", "suit": "HEARTS", "number": 7}
    EIGHT_HEARTS = {"id_": 20, "view": "♥8", "suit": "HEARTS", "number": 8}
    NINE_HEARTS = {"id_": 21, "view": "♥9", "suit": "HEARTS", "number": 9}
    TEN_HEARTS = {"id_": 22, "view": "♥10", "suit": "HEARTS", "number": 10}
    JACK_HEARTS = {"id_": 23, "view": "♥11", "suit": "HEARTS", "number": 11}
    QUEEN_HEARTS = {"id_": 24, "view": "♥12", "suit": "HEARTS", "number": 12}
    KING_HEARTS = {"id_": 25, "view": "♥13", "suit": "HEARTS", "number": 13}
    ACE_TILES = {"id_": 26, "view": "♦A", "suit": "TILES", "number": 1}
    TWO_TILES = {"id_": 27, "view": "♦2", "suit": "TILES", "number": 2}
    THREE_TILES = {"id_": 28, "view": "♦3", "suit": "TILES", "number": 3}
    FOUR_TILES = {"id_": 29, "view": "♦4", "suit": "TILES", "number": 4}
    FIVE_TILES = {"id_": 30, "view": "♦5", "suit": "TILES", "number": 5}
    SIX_TILES = {"id_": 31, "view": "♦6", "suit": "TILES", "number": 6}
    SEVEN_TILES = {"id_": 32, "view": "♦7", "suit": "TILES", "number": 7}
    EIGHT_TILES = {"id_": 33, "view": "♦8", "suit": "TILES", "number": 8}
    NINE_TILES = {"id_": 34, "view": "♦9", "suit": "TILES", "number": 9}
    TEN_TILES = {"id_": 35, "view": "♦10", "suit": "TILES", "number": 10}
    JACK_TILES = {"id_": 36, "view": "♦11", "suit": "TILES", "number": 11}
    QUEEN_TILES = {"id_": 37, "view": "♦12", "suit": "TILES", "number": 12}
    KING_TILES = {"id_": 38, "view": "♦13", "suit": "TILES", "number": 13}
    ACE_CLOVERS = {"id_": 39, "view": "♣A", "suit": "CLOVERS", "number": 1}
    TWO_CLOVERS = {"id_": 40, "view": "♣2", "suit": "CLOVERS", "number": 2}
    THREE_CLOVERS = {"id_": 41, "view": "♣3", "suit": "CLOVERS", "number": 3}
    FOUR_CLOVERS = {"id_": 42, "view": "♣4", "suit": "CLOVERS", "number": 4}
    FIVE_CLOVERS = {"id_": 43, "view": "♣5", "suit": "CLOVERS", "number": 5}
    SIX_CLOVERS = {"id_": 44, "view": "♣6", "suit": "CLOVERS", "number": 6}
    SEVEN_CLOVERS = {"id_": 45, "view": "♣7", "suit": "CLOVERS", "number": 7}
    EIGHT_CLOVERS = {"id_": 46, "view": "♣8", "suit": "CLOVERS", "number": 8}
    NINE_CLOVERS = {"id_": 47, "view": "♣9", "suit": "CLOVERS", "number": 9}
    TEN_CLOVERS = {"id_": 48, "view": "♣10", "suit": "CLOVERS", "number": 10}
    JACK_CLOVERS = {"id_": 49, "view": "♣11", "suit": "CLOVERS", "number": 11}
    QUEEN_CLOVERS = {"id_": 50, "view": "♣12", "suit": "CLOVERS", "number": 12}
    KING_CLOVERS = {"id_": 51, "view": "♣13", "suit": "CLOVERS", "number": 13}
    
    @staticmethod
    def from_number(number: int) -> CardValue:
        """
        Return card value from number.
        """
        for cv in CardValue:
            if cv.value["id_"] == number:
                return cv
            
class Card:
    """
    Card
    """
    def __init__(self, value: CardValue) -> None:
        self.value = value

    def __str__(self) -> str:
        return str(self.value.value["view"])

    def __repr__(self) -> str:
        return str(self)

    def __hash__(self) -> int:
        return int(self.value.value["num"])

    def __eq__(self, other: Card) -> bool:
        return self.value == other.value

    @staticmethod
    def from_number(number: int) -> Card:
        """
        Return card which have card value from number.
        """
        return Card(CardValue.from_number(number=number))
