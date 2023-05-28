"""
HandValidation
"""


from collections import Counter
from typing import List
from .card import Card
from .log import logger


class Validation:
    """
    Nintendo rule.
    """

    def __init__(self) -> None:
        pass

    def __all_different_number(self, hand: List[Card]) -> bool:
        """
        Validate all card number is different.
        """
        return (
            hand[0].number
            != hand[1].number
            != hand[2].number
            != hand[3].number
            != hand[4].number
        )

    def __all_same_suit(self, hand: List[Card]) -> bool:
        """
        Validate all card suit is same.
        """
        return (
            hand[0].suit == hand[1].suit == hand[2].suit == hand[3].suit == hand[4].suit
        )

    def __is_royal_hand(self, hand: List[Card]) -> bool:
        """
        Royal hand: 10, J ,Q, K, A
        """
        return all(
            [
                hand[0].number == 1,
                hand[1].number == 10,
                hand[2].number == 11,
                hand[3].number == 12,
                hand[4].number == 13,
            ]
        )

    def is_royal_straight_flash(self, hand: List[Card]) -> bool:
        """
        Validate hand is whether Royal Straight Flash.
        """
        if (
            abs(hand[0].number - hand[-1].number) == 4
            and self.__all_different_number(hand=hand)
            and self.__all_same_suit(hand=hand)
            and self.__is_royal_hand(hand=hand)
        ):
            logger.info("[HAND] ROYAL STRAIGHT FLASH")
            return True
        else:
            return False

    def is_straight_flash(self, hand: List[Card]) -> bool:
        """
        Validate hand is whether Straight Flash.
        """
        if (
            abs(hand[0].number - hand[-1].number) == 4
            and self.__all_different_number(hand=hand)
            and self.__all_same_suit(hand=hand)
        ):
            logger.info("[HAND] STRAIGHT FLASH")
            return True
        else:
            return False

    def is_four_card(self, hand: List[Card]) -> bool:
        """
        Validate hand is four card.
        """
        counted = Counter(hand)
        keys = list(counted.keys())
        if counted[keys[0]] == 4 or counted[keys[1]] == 4:
            logger.info("[HAND] FOUR CARD")
            return True
        else:
            return False
