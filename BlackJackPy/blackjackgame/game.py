# Salvador Felipe
# CPSC 386-01
# 2022-03-31
# sfel@csu.fullerton.edu
# @SalFell
#
# Lab 03-00
#
# This BlackJackGame file defines the game loop
#

import pickle
from time import sleep
from .cards import Deck, card_value, rank
from .player import Player, Dealer


class BJGame:
    """Class to define game loop."""

    def __init__(self):
        self._players = []

    @classmethod
    def winners(cls, _players):
        """Keeps track of players who have not busted."""
        winner = []
        for player in _players:
            if player.score1 <= 21 and player.score1 > Dealer.score1:
                winner.append(player)
        return winner

    def run(self):
        """Defines game loop."""

        print('Welcome to BlackJack!')
        # Create, merge, and cut 8 decks.
        deck = Deck()
        for _ in range(1, 9):
            deck.merge(Deck(10, len(deck)))
        deck.shuffle()
        deck.cut()

        # Get amount of players
        num_players = int(input('How many players? [1-4]\n>>> '))

        # Get player names
        for i in range(num_players):
            name = input('Player {}, what is your name?\n>>> '.format(i + 1))
            self._players.append(Player(name))

        self._players.append(Dealer(self))
        # try:
            # with open('some random file', 'r') as fh:
                # fh.read()
        # except FileNotFoundError:
            # print('No file found. oh well.')

        dealer = self._players[-1]
        players = self._players

        print('Table: {}'.format(players))
        # Ask for wagers
        for i in range(0, num_players):
            players[i].wager()

        # Initial deal of 2 cards
        current_player_index = 0
        cplayer = players[current_player_index]
        #for i in range(3):
         #   cplayer.hand1.append(deck.deal())
          #  cplayer = players[(current_player_index + i) % len(players)]
            # chang above to deck.deal() for normal game

        for player in players:
            player.hand1.append(deck.deal(2))

        current_player_index = 0

        while True:
            cplayer = players[current_player_index]
            if cplayer == dealer:
                print('\n{} is up!'.format(dealer))
                print('HAND:{}'.format(dealer.hand1))
                print('SCORE: {}'.format(dealer.score1))
            else:
                print('\n{} is up!'.format(cplayer))
                print('{}\'s BALANCE: ${}.00'.format(cplayer, cplayer.balance))
                print('HAND:{}'.format(cplayer.hand1))
                print('SCORE: {}'.format(cplayer.score1))
                print('CHAD\'s HAND: {}, [[Hidden card]]'.format(
                    dealer.hand1[0]))

            if cplayer.score1 == 21:
                # cplayer.balance += cplayer.bet
                print(
                    '''Black Jack!\nYou win!\n
                       You earned: ${}\n
                       Your Balance is now: ${}'''.format(
                           cplayer.bet, cplayer.balance + cplayer.bet)
                )
                cplayer.balance += cplayer.bet
            # Ask player to split if possible.
            if (
                    rank(cplayer.hand1[0][0]) == rank(cplayer.hand1[1][0])
                    and cplayer != dealer
                    and cplayer.bet * 2 <= cplayer.balance
                    and not cplayer.has_split
            ):
                if cplayer.splits():
                    cplayer.hand1.append(deck.deal())
                    cplayer.hand2.append(deck.deal())

                    print('{}\'s BALANCE: ${}.00'.format(
                        cplayer, cplayer.balance))
                    print('HAND ONE:{}'.format(cplayer.hand1))
                    print('SCORE: {}'.format(cplayer.score1))
                    print('CHAD\'s HAND: {}, [[Hidden card]]'.format(
                        dealer.hand1[0]))

                    while cplayer.hits() and cplayer.score1 < 21:
                        cplayer.hand1.append(deck.deal())
                        print('{}\'s BALANCE: ${}.00'.format(
                            cplayer, cplayer.balance))
                        print('HAND ONE:{}'.format(cplayer.hand1))
                        print('SCORE: {}'.format(cplayer.score1))
                        print('CHAD\'s HAND: {}, [[Hidden card]]'.format(
                            dealer.hand1[0]))

                        # Ask player to double down.
                        if not cplayer.has_doubled:
                            cplayer.double_down()
                        print('BET: ${}'.format(cplayer.bet))

                        # Ask for insurance
                        if card_value(dealer.hand1[0][0]) == 10:
                            if cplayer != dealer:
                                resp = input(
                                    'Would you like to buy \
                                     insurance? Y/N\n>>> '
                                )
                                if resp.lower() == 'y':
                                    cplayer.ask_side_bet()
                        continue

                    while cplayer.hits() and cplayer.score2 < 21:
                        cplayer.hand2.append(deck.deal())
                        print('{}\'s BALANCE: ${}.00'.format(
                            cplayer, cplayer.balance))
                        print('HAND TWO:{}'.format(cplayer.hand2))
                        print('SCORE: {}'.format(cplayer.score2))
                        print('CHAD\'s HAND: {}, [[Hidden card]]'.format(
                            dealer.hand1[0]))

                        # Ask player to double down.
                        if not cplayer.has_doubled:
                            cplayer.double_down()
                        print('BET: ${}'.format(cplayer.bet))

                        # Ask for insurance
                        if card_value(dealer.hand1[0][0]) == 10:
                            if cplayer != dealer:
                                resp = input(
                                    'Would you like to buy \
                                     insurance? Y/N\n>>> '
                                )
                                if resp.lower() == 'y':
                                    cplayer.ask_side_bet()
                        continue

            # Ask player to double down.
            if not cplayer.has_doubled:
                cplayer.double_down()
                print('BET: ${}'.format(cplayer.bet))

            # while cplayer.hits() and cplayer.score1 < 21:

            # Ask for insurance
            if card_value(dealer.hand1[0][0]) == 10:
                if cplayer != dealer:
                    resp = input(
                        '''Would you like to buy
insurance? Y/N\n>>> '''
                    )
                if resp.lower() == 'y':
                    cplayer.ask_side_bet()

            # Ask player to hit.
            if cplayer.hits():
                cplayer.hand1.append(deck.deal())
                print('HAND:{}'.format(cplayer.hand1))
                print('SCORE: {}'.format(cplayer.score1))
                print('CHAD\'s HAND: {}'.format(dealer.hand1[0]))

                if cplayer.score1 > 21:
                    print('BUSTED! You went over 21!')
                    print('You lost: ${}'.format(cplayer.bet))
                    print('Your Balance is now: ${}'.format(
                        cplayer.balance - cplayer.bet))
                    current_player_index = (current_player_index + 1) % len(
                        self._players
                    )
            else:
                print('{} is HOLDING.'.format(cplayer))
                current_player_index = (current_player_index + 1) % len(
                    self._players
                )

            if deck.needs_shuffling():
                for _ in range(1, 9):
                    deck.merge(Deck(10, len(deck)))
                deck.shuffle()
                deck.cut()

            if dealer.score1 > 21:
                print('Dealer BUSTED!')
                sleep(2)
                print('Winning players: {}'.format(BJGame.winners(players)))
                for player in players:
                    player.bankroll += player.bet
                    print('{}\'s BALANCE: ${}'.format(player, player.balance))
            continue
            # sleep(2)
