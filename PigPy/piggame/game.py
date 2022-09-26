# Salvador Felipe
# CPSC 386-01
# 2022-03-01
# sfel@csu.fullerton.edu
# @SalFell
#
# Lab 02-00
#
# This is the piggame file that defines the game loop
#

"""
Defines game loop for Pig Game

Classes:

    PigGame

Functions:

    __init__(self)
    am_i_real(self)
    opponent_score(self, me)
    run(self)

Misc Variables:

    self._players
    rules
    die
    num_players
    name
    order
    key
    current_player_index
    cplayer
    rolled_number
    cplayer.rolls
    cplayer.turn_score
    cplayer.score
"""

import time
from .die import Die
from .player import Player, ComputerPlayer


class PigGame:

    """
    A class to represent the game.

    ...

    Methods
    -------
    am_i_real():
        returns statement "If your asking me, your not"
    opponent_score(me):
        returns human player score to computer player
    run():
        "Pig Game" game loop
    """

    def __init__(self):

        """
        Constructs array to be populated with player objects

        Parameters
        ----------
        None

        Returns
        -------
        None
        """

        self._players = []

    @classmethod
    def am_i_real(cls):

        """
        Allows communication between the game and the computer AI

        Parameters
        ----------
        None

        Returns
        ------
        statement "If your asking, me your not"
        """

        return 'If your asking me, your not'

    def opponent_score(self, comp):

        """
        Obtains score of human player for computer AI's behavior

        Parameters
        ----------
        comp :
            computer AI object

        Returns
        -------
        player.score(int): human player's score at current game state
        """
        for player in self._players:
            if comp != player:
                return player.score
            return False

    def run(self):

        """
        Defines game loop

        Parameters
        ----------
        None

        Returns
        -------
        None
        """
        print('Welcome to Pig Game!')
        rules = """
            Rules

            * To start the game, you may enter the number 1 through 4
              to establish how many players there are.
              If you enter 1, then the other player is a computer AI.
            * When you enter 2 or more players, then the computer AI
              is not used as a player.
            * There is one six-sided die (simulated by the game using
              a psuedo-random number generator).
            * The game is turn based.
            * All players have a name, including the computer AI.
            * The player who goes first is selected by each player
              rolling the die once.
              The players are ordered in ascending order given the
              number they rolled.
              If there is a tie between two or more players, the
              computer can break the tie
              by arbitrarily assigning that player to a position not
              less than the position the player rolled.
            * Once each player has had a turn in ascending order, the
              turn returns to the first player.
              (The process is a circular queue.)
            * Each turn, a player rolls the die.
                * The current player rolls the die until their turn ends.
                  All other players wait their turn.
                  A turn ends when a player rolls a 1 or chooses to hold.
                * If the player rolls a 1, the player scores nothing that
                  turn and it becomes the next player's turn.
                  The player's overall score does not change because the
                  player has lost the points accrued during their turn.
                * If the player rolls any other number, the value of the
                  die is added to their turn's score as points and the
                  player's turn may continue.
                  The player's overall score does not change until their
                  turn ends.
                * If a player chooses to hold, their turn score total is
                  added to their score, and it becomes the next player's turn.
            * The player may not choose to hold until after the die has been
              rolled at least once.
            * The game ends when a player ends their turn with a score of 30
              points or greater.
            * At the beginning of every die roll, the game displays the current
              player's total score, current turn score, and how many times the
              player has rolled.
              Once the die is rolled, the computer displays the value of the
              die. If it is a 1, the computer ends the current player's turn
              and moves on to the next player.

        """
        print(rules)
        die = Die()
        # asks for how many humans are playing
        num_players = int(input('How many players? [1-4]\n>>> '))

        # asks for name, rolls for order, tells where the player falls in line
        for i in range(num_players):
            name = input('Player {}, what is your name?\n>>> '.format(i + 1))
            order = die.roll()
            print('You rolled {}.'.format(order))
            self._players.append(Player(name, order))

        if num_players == 1:
            order = die.roll()
            self._players.append(ComputerPlayer(order, self))

        self._players.sort(key=lambda p: p.order)
        print(self._players)
        current_player_index = 0

        while True:
            cplayer = self._players[current_player_index]
            print('\n{} is up!'.format(cplayer))
            print('{}\'s total score: {}'.format(cplayer, cplayer.score))
            print('{}\'s turn score: {}'.format(cplayer, cplayer.turn_score))
            print(
                '{}\'s number of rolls this game: {}'.format(
                    cplayer, cplayer.rolls
                )
            )
            rolled_number = die.roll()
            if rolled_number == 1:
                cplayer.rolls += 1
                cplayer.turn_score = 0
                print(
                    '''You rolled a 1.
                No points for this turn.
                Your turn is over.'''
                )
                current_player_index = (current_player_index + 1) % len(
                    self._players
                )
                time.sleep(2)
                continue
            if cplayer.turn_score >= 30 or (
                cplayer.score + cplayer.turn_score + rolled_number >= 30
            ):
                print('You rolled: {}'.format(rolled_number))
                print(
                    '{} reached the score limit of 30 and won!'.format(cplayer)
                )
                break
            if rolled_number != 1 and (
                cplayer.turn_score >= 30
                or (cplayer.score + cplayer.turn_score + rolled_number <= 30)
            ):
                print('You rolled: {}'.format(rolled_number))
                time.sleep(2)

            if cplayer.roll_again():
                cplayer.rolls += 1
                cplayer.turn_score += rolled_number
            else:
                print('{} is holding.'.format(cplayer))
                cplayer.turn_score += rolled_number
                cplayer.score += cplayer.turn_score
                cplayer.turn_score = 0
                current_player_index = (current_player_index + 1) % len(
                    self._players
                )
                time.sleep(2)

            time.sleep(2)
