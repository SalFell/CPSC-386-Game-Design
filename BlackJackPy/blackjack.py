#!/usr/bin/env python3
# Salvador Felipe
# CPSC 386-01
# 2022-03-31
# sfel@csu.fullerton.edu
# @SalFell
#
# Lab 03-00
#
# This is the BlackJackGame file that runs the game
#

"""
Main file of BlackJack Game.

Misc Variables:
    GAME
"""

from blackjackgame import game, __init__

if __name__ == '__main__':
    GAME = game.BJGame()
    GAME.run()
