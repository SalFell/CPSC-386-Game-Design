# Salvador Felipe
# CPSC 386-01
# 2022-03-31
# sfel@csu.fullerton.edu
# @SalFell
#
# Lab 03-00
#
# This BlackJackGame file defines the Player and Dealer classes.
#

from .cards import score


class Player:
    """Class to represent player object."""

    def __init__(self, name, bankroll=10000):
        self._name = name
        self._balance = bankroll
        self._bet = 0
        self._side_bet = 0
        self._hand = [[], []]
        self.has_doubled = False
        self._did_split = False
        self._score1 = 0
        self._score2 = 0

    @property
    def name(self):
        """Returns player name."""
        return self._name

    @property
    def balance(self):
        """Returns player balance."""
        return self._balance

    @property
    def bet(self):
        """Returns player bet."""
        return self._bet

    @property
    def side_bet(self):
        """Returns player side bet."""
        return self._side_bet

    @property
    def hands(self):
        """Returns player's hands."""
        return self._hand

    @property
    def hand1(self):
        """Returns player's first hand."""
        return self._hand[0]

    @property
    def hand2(self):
        """Returns player's second hand."""
        return self._hand[1]

    @property
    def score1(self):
        """Check the player's score."""
        self._score1 = score(self._hand[0])
        return self._score1

    @property
    def score2(self):
        """Check the player's score."""
        self._score2 = score(self._hand[1])
        return self._score2

    def __str__(self):
        return self._name

    def __repr__(self):
        return 'Player("{}")'.format(self._name)

    def has_split(self):
        """Checks if player has split."""
        return len(self._hand[1] == 0)

    @classmethod
    def hits(cls):
        """Asks player if they want to hit or stand.
        Returns True if hits."""

        resp = input('Will you hit or stand? H/S\n>>> ')
        if resp.lower() == 'h':
            return True
        return False

    def splits(self):
        """Asks player if they want to split their
        hand when they have two cards of identical
        rank. Returns True if does split."""

        resp = input('Would you like to split? Y/N\n>>> ')
        if resp.lower() == 'y':
            self._did_split = True
            # self._hand2 = [self._hand1[:-1]]
            # self._hand1 = [self._hand[0]]
            self._hand[1] = [self._hand[0][-1]]
            self._hand[0] = [self._hand[0][0]]
            return True
        return False

    def wager(self):
        """Asks player how much they would like to bet."""

        resp = int(
            input(
                '''{}, please place your bet to the
nearest dollar please.\n>>> $'''.format(self._name)
            )
        )
        if resp <= self._balance:
            self._bet += resp
            self._balance -= resp
        else:
            resp = int(input(
                '''Insufficient funds.
Please try again.\n>>> $'''
            ))
            self._bet += resp
            self._balance -= resp

    @classmethod
    def insurance(cls):
        """Asks player if they want to buy
        insurance. Returns True if yes."""

        resp = input(
            'Would you like to buy insurance? Y/N\n>>> '
        )
        if resp.lower() == 'y':
            return True
        return False

    def ask_side_bet(self):
        """Asks player how much they would like
           to place as their side bet."""

        resp = int(
            input(
                '''How much insurance would you
like to bet [$1-${}](To the nearest dollar please)?
>>> $'''.format(self._balance - self._bet)
            )
        )
        if resp <= self._balance:
            self._side_bet += resp
        else:
            resp = int(
                input(
                    '''Insufficient funds.
Please try again.\n>>>$'''
                )
            )
            self._side_bet += resp

    def double_down(self):
        """Asks player if they want to double
        down. Returns True if yes, False
        otherwise."""

        if self._bet * 2 <= self._balance:
            resp = input(
                '''Would you like to double down?
Y/N\n>>> '''
            )
            if resp.lower() == 'y':
                self.has_doubled = True
                self._balance -= self._bet
                self._bet += self._bet
                return True
        else:
            print(
                '''Insufficient funds. Can not
                   double down.'''
            )
            return False


class Dealer(Player):
    """A class to represent the dealer player object."""

    def __init__(self, game):
        super().__init__("CHAD")
        self._game = game

    def __repr__(self):
        return 'Dealer("{}")'.format(self._name)

    def hits(self):
        """Checks to see if the dealer hits. If their
        hand is less than 17, then they can hit."""
        self_score = self._game._score(self)
        bool(self_score < 17)
