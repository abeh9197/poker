"""
main.py
"""

from models import Deck, Game, Player, Validation
from utils.log import logger


def main() -> None:
    """
    TODO: Playerの人数は可変とする。
    """
    count = 0
    validator = Validation()
    while True:
        count += 1
        logger.info("COUNT: %s", count)
        deck = Deck()
        deck.shuffle()
        game = Game(deck=deck)

        game.deck.shuffle()
        cards = game.deal()
        player = Player(cards=cards)
        player.hand = sorted(player.hand, key=lambda x: x.number)
        logger.info(player.hand)
        if validator.judge_hand(hand=player.hand):
            break


if __name__ == "__main__":
    main()
