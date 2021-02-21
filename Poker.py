from Player import Player
from Card import Card
from random import shuffle    

class Poker():

    global deck, suits, ids, values, players
    global numPlayers, numChips
    players = []
    deck = []
    suits = ['D','H','S','C']
    ids = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
    values = [2,3,4,5,6,7,8,9,10,11,12,13,14]

    # initialize deck
    for i in range(len(ids)):
        for j in range(len(suits)):
            card = Card(suits[j], ids[i], values[i])
            deck.append(card)

    def __init__(self):
        shuffle(deck)
        self.initialDeal()

    numChips = 10
    def initialDeal(self):
        # TODO: create players
        # TODO: deal cards
        numPlayers = int(input('how many people are playing: '))
        for i in range(numPlayers):
            players.append(Player(numChips))
        
        print(players[0].card1.id + players[0].card1.suit +
              ", " + players[0].card2.id + players[0].card2.suit)
        
        '''
        players[0] = Player(numChips, deck[0], deck[1])
        player2 = Player(numChips, deck[2], deck[3])
        print(player1.card1.id + player1.card1.suit +
              ", " + player1.card2.id + player1.card2.suit)
        print(player2.card1.id + player2.card1.suit +
              ", " + player2.card2.id + player2.card2.suit)
        '''





'''
    def checkHands():


    def preflop():
        # TODO: assign blinds
        # TODO: checks and bets
        # TODO: update pot
        # TODO: winner?

    def flop():
        # TODO: flip three cards from deck
        # TODO: checks and bets
        # TODO: update pot
        # TODO: winner?

    def turn(playerBank, label):
        # TODO: burn one card
        # TODO: flip another
        # TODO: checks and bets
        # TODO: update pot
        # TODO: winner?
        
        action = input('do you want to check, call, raise or fold? ')
        if action == 'check':
            pass
        elif action == 'call':
            bet = int(input('how much was the original bet? '))
            playerBank -= bet
            pot += bet
        elif action == 'raise':
            bet = int(input('how much do you want to raise? '))
            pot += bet
            playerBank = playerBank - bet
        elif action == 'fold':
            Aichips += pot
        
        for k in range(Players):
            turn

    def river():
        # TODO: burn one card
        # TODO: flip another
        # TODO: checks and bets
        # TODO: update pot
        # TODO: determine winner
        # TODO: distribute pot
        
'''
