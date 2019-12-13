import random
from datetime import datetime

SUITS = ["d", "c", "h", "s"]
RANKS = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]


class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def value(self):
        if self.is_ace:
            return 11
        elif self.rank in "J Q K".split():
            return 10
        return int(self.rank)

    @property
    def is_ace(self):
        return self.rank == "A"


class Deck:
    def __init__(self):
        self.cards = [Card(suit, rank) for suit in SUITS for rank in RANKS]
        self.shuffle()

    def shuffle(self):
        random.shuffle(self.cards)

    def deal_card(self):
        return self.cards.pop(0)


class Hand:
    def __init__(self):
        self.hand = []

    def add_card(self, card):
        self.hand.append(card)

    def check_hand(self):
        value = sum([card.value() for card in self.hand])
        num_aces = sum([card.is_ace for card in self.hand])
        while value > 21 and num_aces > 0:
            value -= 10
            num_aces -= 1
        return value
