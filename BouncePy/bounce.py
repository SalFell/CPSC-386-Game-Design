#! /usr/bin/env python3
# Salvador Felipe
# CPSC 386-01
# 2022-04-25
# sfel@csu.fullerton.edu
# @SalFell
#
# Lab 05-00
#
# File that contains the main program.
#


"""
Imports the Bounce demo and executes the main function.
"""

import sys
from game import game

if __name__ == "__main__":
    NUM_BALLS = 5
    if len(sys.argv) > 1:
        NUM_BALLS = int(sys.argv[1])
    if NUM_BALLS >= 50:
        NUM_BALLS = 49
    NUM_BALLS = max(NUM_BALLS, 3)
    video_game = game.BounceDemo(NUM_BALLS)
    video_game.build_scene_graph()
    video_game.run()
