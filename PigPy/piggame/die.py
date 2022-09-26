# Salvador Felipe
# CPSC 386-01
# 2022-03-01
# sfel@csu.fullerton.edu
# @SalFell
#
# Lab 02-00
#
# This is the piggame file that defines a six sided die
#

"""
Defines a six sided die class for Pig Game

Classes:

    Die

Functions:

    __init__(self)
    roll(cls)
    other_roll(cls)
"""

from random import randrange, randint


class Die:

    """
    A class to represent a die.

    ...

    Methods
    -------
    roll()
        Returns a random number from 1 to 6
    """

    def __init__(self):

        """
        Constructs necessary attributes for die object

            Parameters
            ----------
            None

            Returns
            -------
            None
        """

    @classmethod
    def roll(cls):

        """
        Returns a random number from 1 to 6, inclusive

            Parameters:
                    None

            Returns:
                    randrange(1, 7): a random number from 1 to 6
        """

        return randrange(1, 7)

    @classmethod
    def other_roll(cls):

        """
        Another way to get a random number from 1 to 6.
        Returns a random number from 1 to 6.

            Parameters:
                None

            Returns:
                randint(1,6): a random number from 1 to 6
        """

        return randint(1, 6)
