"""
Tests for hand validation.
"""


import unittest
from src.models import Card, Validation


class TestValidation(unittest.TestCase):
    """
    Test validations.
    """

    def test_is_royal_straight_flash(self):
        """
        Test method for is_royal_straight_flash.
        """
        validator = Validation()
        hand_royal_straight_flash = [Card.from_number(0)] + [
            Card.from_number(id_) for id_ in range(9, 13)
        ]
        self.assertTrue(
            validator.is_royal_straight_flash(hand=hand_royal_straight_flash)
        )

    def test_is_four_card(self):
        """
        Test method for is_four_card.
        """
        validator = Validation()
        hand_four_card = [
            Card.from_number(0),
            Card.from_number(0),
            Card.from_number(0),
            Card.from_number(0),
        ] + [Card.from_number(3)]
        print(hand_four_card)
        self.assertTrue(validator.is_four_card(hand=hand_four_card))
