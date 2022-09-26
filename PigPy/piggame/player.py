# Salvador Felipe
# CPSC 386-01
# 2022-03-01
# sfel@csu.fullerton.edu
# @SalFell
#
# Lab 02-00
#
# This piggame file defines the human and computer player class
#

"""
Creates Player and Computer AI objects

Classes:

    Player
    ComputerPlayer

Functions:

    __innit__(self, name, order)
    name(self)
    order(self)
    score(self)
    score(self, new_score)
    turn_score(self)
    turn_score(self, new_turn_score)
    rolls(self)
    rolls(self, num_rolls)
    roll_again(cls)
    am_i_human(cls)
    are_you_real(cls)
    __str__(self)
    __repr__(self)
    __init__(self, order, game)
    am_i_human(self)
    are_you_real(self)
    roll_again(self)

Misc Variables:

    self._name
    self._score
    self._turn_score
    self._order
    self._rolls
    resp
    self._game
    opponent_score
"""


class Player:

    """
    A class to represent the player

    ...

    Attributes
    ----------
    name : str
        name of the player
    order : int
        player\'s position in terms of who\'s turn it is

    Methods
    -------
    name()
        Returns player name.
    order()
        Returns player position in turn cycle.
    score()
        Returns player score.
    score(new_score)
        Increases player score to new score.
    turn_score()
        Returns player\'s turn score.
    turn_score(new_turn_score)
        Increases player\'s turn score to new turn score.
    rolls()
        Returns amount of times player has rolled.
    rolls(num_rolls)
        Increases amount of times player has rolled.
    roll_again(cls)
        Asks player if they want to roll or hold.
        Returns True if player rolls.
        Returns False if player holds.
    am_i_human(cls)
        Helps player object communicate with the game.
        Returns True.
    are_you_real(cls)
        Helps player object communicate with the game.
        Returns statement "Yes I am human".
    __str__(self)
        Returns player name.
    __repr__(self)
        Returns representation of player as ("player name", player order).
    """

    def __init__(self, name, order):

        """
        Constructs necessary attributes for player object.

        Parameters
        ----------
            name : str
                player name
            order : int
                player\'s position in terms of who\'s turn it is
        """
        self._name = name
        self._score = 0
        self._turn_score = 0
        self._order = order
        self._rolls = 0

    @property
    def name(self):

        """
        Returns player name.

        Parameters
        ----------
        None

        Returns
        -------
        Player name
        """
        return self._name

    @property
    def order(self):

        """
        Returns player position in turn cycle.

        Parameters
        ----------
        None

        Returns
        -------
        Player position in turn cycle
        """
        return self._order

    @property
    def score(self):

        """
        Returns player current score.

        Parameters
        ----------
        None

        Returns
        -------
        Player current score
        """
        return self._score

    @score.setter
    def score(self, new_score):
        self._score = new_score

    @property
    def turn_score(self):

        """
        Returns player\'s score for the current turn.

        Parameters
        ----------
        None

        Returns
        -------
        Player\'s score for current turn
        """
        return self._turn_score

    @turn_score.setter
    def turn_score(self, new_turn_score):
        self._turn_score = new_turn_score

    @property
    def rolls(self):

        """
        Returns amount of times player has rolled in the current game.

        Parameters
        ----------
        None

        Returns
        -------
        Amount of times player has rolled in the current game.
        """
        return self._rolls

    @rolls.setter
    def rolls(self, num_rolls):
        self._rolls = num_rolls

    @classmethod
    def roll_again(cls):

        """
        Asks human player if they want to roll or hold.
        Returns True or False accordingly.

        Parameters
        ----------
        None

        Returns
        -------
        True if player wants to roll
        False if player wants to hold
        """
        resp = input("Do you want to roll or hold? (R/H)\n>>> ")
        if resp.lower() == 'r':
            return True
        return False

    @classmethod
    def am_i_human(cls):

        """
        Helps player object communicate with the game.
        Returns True.

        Parameters
        ----------
        None

        Returns
        -------
        True
        """
        return True

    @classmethod
    def are_you_real(cls):

        """
        Helps player object communicate with the game.
        Returns a statement.

        Parameters
        ----------
        None

        Returns
        -------
        'Yes I am human'
        """
        return 'Yes I am human'

    def __str__(self):
        return self._name

    def __repr__(self):
        return 'Player("{}", {})'.format(self._name, self._order)


class ComputerPlayer(Player):

    """
    A class to represent the computer player object

    ...

    Attributes
    ----------
    order : int
        player\'s position in terms of who\'s turn it is
    game : game object
        computer player is an extension of the game

    Methods
    -------
    am_i_human():
        Returns False.
    are_you_real():
        Asks game if it is real.
        Returns statement "If your asking me, your not."
    roll_again():
        Checks if human player's score is over 20.
        Returns True if is, False if not
    """

    def __init__(self, order, game):
        super().__init__("AL", order)
        self._game = game

    def am_i_human(self):
        return False

    def are_you_real(self):
        return self._game.am_i_real()

    def roll_again(self):
        opponent_score = self._game.opponent_score(self)
        bool(opponent_score >= 20)
