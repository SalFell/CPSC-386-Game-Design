#!/usr/bin/env python3
# Salvador Felipe
# CPSC 386-01
# 2022-03-01
# sfel@csu.fullerton.edu
# @SalFell
#
# Lab 02-00
#
# This is the piggame file that runs the game
#

"""
Main file of Pig Game.

Misc Variables:
    GAME
"""

from piggame import game, __init__

if __name__ == '__main__':
    GAME = game.PigGame()
    GAME.run()
