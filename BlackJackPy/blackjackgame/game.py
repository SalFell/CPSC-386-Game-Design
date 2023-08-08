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

def to_file(pickle_file, players):
    """Writes player data to file."""
    with open(pickle_file, 'wb') as fh:
        pickle.dump(players, fh, pickle.HIGHEST_PROTOCOL)

def from_file(pickle_file):
    """Reads player data from file."""
    with open(pickle_file, 'rb') as fh:
        return pickle.load(fh)

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

        # Temporary database of player info
        database = []
        players = self._players
        print('Welcome to BlackJack!')
        # Create, merge, and cut 8 decks.

        # Get amount of players
        num_players = int(input('How many players? [1-4]\n>>> '))

        # Try to open pickle file
        try:
            database = from_file('players.pickle')
            for i in range(num_players):
                name = input(f'Player {i+1}, what is your name?\n>>> ')
                # Try to find player in database
                try:
                    for player in database:
                        if player.name == name:
                            print(f'Welcome back, {name}!')
                            players.append(player)

                            # Check if player still has money
                            if player.balance <= 0:
                                print(f'You have no money left, {name}!'
                                      'An anonymous donor has given you $10000!')
                                player.balance = 10000
                        else:
                            players.append(Player(name))
                except IndexError:
                    players.append(Player(name))
        except FileNotFoundError:
            database = []
            for i in range(num_players):
                name = input(f'Player {i+1}, what is your name?\n>>> ')
                players.append(Player(name))

        # Create, merge, and cut 8 decks.
        deck = Deck()
        for _ in range(1, 9):
            deck.merge(Deck(10, len(deck)))
        deck.shuffle()
        deck.cut()

        # Create dealer
        players.append(Dealer(BJGame))
        dealer = players[-1]

        # Print table
        print(f'Table: {players}')

        # Ask for wagers
        for i in range(0, num_players):
            players[i].wager()

        # Initial deal of 2 cards
        current_player_index = 0
        cplayer = players[current_player_index]

        for player in players:
            player.reset_hands()
            player.hand.extend(deck.deal(2))

        current_player_index = 0

        while True:
            cplayer = players[current_player_index]
            if cplayer == dealer:
                print(f'\n{cplayer} is up!')
                print(f'HAND: {cplayer.hand}')
                print(f'SCORE: {cplayer.score1}')
            else:
                print(f'\n{cplayer} is up!')
                print(f'{cplayer}\'s BALANCE: ${cplayer.balance}')
                print(f'HAND: {cplayer.hand}')
                print(f'SCORE: {cplayer.score1}')
                print(f'CHAD\'s HAND: {dealer.hand[0]}, [[Hidden card]]')

            if cplayer.score1 == 21:
                print(f'''{cplayer} got a Black Jack!\n
                       You earned: ${cplayer.bet}\n
                       Your Balance is now: ${cplayer.balance(cplayer.bet)}''')
                # Increase player balance by bet amount
                cplayer.balance(cplayer.bet)

            # Ask player to split if possible.
            if (
                    rank(cplayer.hand[0]) == rank(cplayer.hand[1])
                    and cplayer != dealer
                    and cplayer.bet * 2 <= cplayer.balance
                    and not cplayer.has_split
            ):
                if cplayer.splits():
                    cplayer.hand.append(deck.deal())
                    cplayer.hand2.append(deck.deal())
                    print(f'{cplayer}\'s BALANCE: ${cplayer.balance}')
                    print(f'HAND ONE: {cplayer.hand}')
                    print(f'SCORE: {cplayer.score1}')
                    print(f'HAND TWO: {cplayer.hand2}')
                    print(f'SCORE: {cplayer.score2}')
                    print(f'CHAD\'s HAND: {dealer.hand[0]}, [[Hidden card]]')

                    while cplayer.hits() and cplayer.score1 < 21:
                        cplayer.hand.append(deck.deal())
                        print(f'{cplayer}\'s BALANCE: ${cplayer.balance}')
                        print(f'HAND ONE: {cplayer.hand}')
                        print(f'SCORE: {cplayer.score1}')
                        print(f'CHAD\'s HAND: {dealer.hand[0]}, [[Hidden card]]')

                        # Ask player to double down.
                        if not cplayer.has_doubled:
                            cplayer.double_down()
                        print(f'BET: ${cplayer.bet}')

                        # Ask for insurance
                        if card_value(dealer.hand[0]) == 10:
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
                        print(f'{cplayer}\'s BALANCE: ${cplayer.balance}')
                        print(f'HAND TWO: {cplayer.hand2}')
                        print(f'SCORE: {cplayer.score2}')
                        print(f'CHAD\'s HAND: {dealer.hand[0]}, [[Hidden card]]')

                        # Ask player to double down.
                        if not cplayer.has_doubled:
                            cplayer.double_down()
                        print(f'BET: ${cplayer.bet}')

                        # Ask for insurance
                        if card_value(dealer.hand) == 10:
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
                print(f'BET: ${cplayer.bet}')

            # while cplayer.hits() and cplayer.score1 < 21:

            # Ask for insurance
            if card_value(dealer.hand[0]) == 10:
                if cplayer != dealer:
                    resp = input(
                        '''Would you like to buy
insurance? Y/N\n>>> '''
                    )
                if resp.lower() == 'y':
                    cplayer.ask_side_bet()

            # Ask player to hit.
            if cplayer.hits():
                cplayer.hand.append(deck.deal())
                print(f'HAND: {cplayer.hand}')
                print(f'SCORE: {cplayer.score1}')
                print(f'CHAD\'s HAND: {dealer.hand[0]}')

                if cplayer.score1 > 21:
                    print('BUSTED! You went over 21!')
                    print(f'You lost: ${cplayer.bet}')
                    print(f'Your Balance is now: ${cplayer.balance(-cplayer.bet)}')
                    current_player_index = (current_player_index + 1) % len(
                        self._players
                    )
            else:
                print(f'{cplayer} is HOLDING.')
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
                print(f'Winning players: {BJGame.winners(players)}')
                for player in players:
                    player.bankroll(player.bet)
                    print(f'{player}\'s BALANCE: ${player.balance}')
            continue
            # sleep(2)
