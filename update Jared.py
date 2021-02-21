# -*- coding: utf-8 -*-
"""
Created on Sat Feb 20 21:20:30 2021

@author: jared
"""

from Card import Card
from Player import Player

from Card import Card
from random import shuffle    

deck   = []
suits  = ['D', 'H', 'S', 'C']
ids    = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14']
class Poker():
    deck   = []
    suits  = ['D', 'H', 'S', 'C']
    ids    = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    values = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]

    for i in range(len(ids)):
        for j in range(len(suits)):
            card = Card(suits[j], ids[i], values[i])
            deck.append(card)


    
    def initialDeal():
        # TODO: deal cards
for i in range(len(ids)):
    for j in range(len(suits)):
        card = Card(suits[j], ids[i], values[i])
        deck.append(card)
        
    def preflop():
        # TODO: assign Blinds
Pot = 3
BBlind = True

while BBlind:
    Player.numChips - 2
    Pot += 2
        
SBlind = True 

while SBlind:
    Player.numChips - 1
    Pot += 1
    
        # TODO: checks and bets
        # TODO: update pot
        # TODO: winner?
for i in range(len(deck)):
    print(deck[i].id + deck[i].suit)
    def flop():
        # TODO: flip three cards from deck
        # TODO: checks and bets
        # TODO: update pot
        # TODO: winner?
    def turn():
        # TODO: burn one card
        # TODO: flip another
        # TODO: checks and bets
        # TODO: update pot
        # TODO: winner?
    def river():
        # TODO: burn one card
        # TODO: flip another
        # TODO: checks and bets
        # TODO: update pot
        # TODO: determine winner
        # TODO: distribute pot
        
    '''