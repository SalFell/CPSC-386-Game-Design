# Salvador Felipe
# CPSC 386-01
# 2022-03-31
# sfel@csu.fullerton.edu
# @SalFell
#
# Lab 03-00
#
# This BlackJackGame file defines a 52 card deck.
#

"""Deck class of 52 French suited cards."""

from collections import namedtuple
from random import shuffle, randrange
from math import floor

Card = namedtuple('Card', ['rank', 'suit'])


def _str_card(card):
    """Convert a card to a nicely formatted string."""
    return f'{card.rank} of {card.suit}'


class Deck:
    """Deck class of 52 French suited cards"""

    ranks = ['Ace'] + [str(x) for x in range(2, 11)] + \
    'Jack Queen King'.split()
    suits = 'Clubs Hearts Spades Diamonds'.split()
    values = list(range(1, 11)) + [10, 10, 10]
    values_dict = dict(zip(ranks, values))

    def __init__(self, cut_card_position_min=0, cut_card_position_max=0):
        """Create a new deck with a cut card."""

        if cut_card_position_max == 0 and cut_card_position_min == 0:
            self._cut_card_position = 0
        else:
            self._cut_card_position = randrange(
                cut_card_position_min, cut_card_position_max
            )
        self._cards = [
            Card(rank, suit) for suit in self.suits for rank in self.ranks
        ]

    def get_cards(self):
        """Return the cards in the deck."""
        return self._cards
    
    def needs_shuffling(self):
        """Checks if the deck needs to be shuffled based on
        the cut card position."""
        return len(self._cards) <= self._cut_card_position

    def __getitem__(self, position):
        """Return the card at the given position."""
        return self._cards[position]

    def __len__(self):
        """Return number of cards in the deck."""
        return len(self._cards)

    def shuffle(self, n_shuffles=1):
        """Shuffle the deck n times. Default is 1 time."""
        for _ in range(n_shuffles):
            shuffle(self._cards)

    def cut(self):
        """Cut the deck at around the half way point
        +/- 20% of the cards."""
        extra = floor(len(self._cards) * 0.2)
        half = (len(self._cards) // 2) + randrange(-extra, extra)
        tophalf = self._cards[:half]
        bottomhalf = self._cards[half:]
        self._cards = bottomhalf + tophalf

    def deal(self, n_cards=1):
        """Deals out cards from the "top" of the deck.
        Default is 1."""
        return [self._cards.pop(0) for _ in range(n_cards)]

    def merge(self, other_deck):
        """Merge the current deck wth the deck passed
        as a parameter."""
        self._cards = self._cards + other_deck._cards

    def __str__(self):
        """Convert the deck to a string."""
        return '\n'.join(map(str, self._cards))


def card_value(card):
    """Return the numerical value of the rank of
    a given card."""
    return Deck.values_dict[card.rank]


def score(hand):
    """Returns the worth of the player's hand."""
    total = 0

    for card in hand:
        total += card_value(card)
    if sum(map(lambda card: card.rank == 'Ace', hand)) and total + 10 <= 21:
        total += 10
    # lambda creates an anonymous function that declares a behavior
    # within an existing function
    return total


def rank(card):
    """Returns the rank of the given card."""
    return card.rank


Card.value = card_value
Card.__int__ = card_value
Card.__str__ = _str_card
