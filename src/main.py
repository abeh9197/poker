"""
main.py
"""

from models import Deck, Game


def main() -> None:
    """
    TODO: Playerの人数は可変とする。
    """
    deck = Deck()
    deck.shuffle()
    game = Game(deck=deck)

    game.deck.shuffle()
    hand = game.deal()
    print(len(game.deck))
    print(hand)


if __name__ == "__main__":
    main()