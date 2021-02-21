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
        self.checksAndBets()
        
    def isWinner():
        pass

    def initialDeal(self):
        # create players
        numPlayers = int(input('how many players are playing? '))
        for i in range(numPlayers):
            numChips = int(input(f'how many chips is player {i+1} buying in for? '))
            players.append(Player(i, numChips))
        
        # deal cards
        count = 0
        for i in range(numPlayers):
            players[i].card1 = deck[count]
            players[i].card2 = deck[count+1]
            count += 2
        
        for i in range(numPlayers):
            players[i].toString()

    def preflop(self):
        # TODO: assign blinds
        # TODO: checks and bets
        # TODO: update pot
        # TODO: winner?

        for i in range(len(players)):
            if players[i].isBlind:
                # big blind bets 2 chips
                # small blind bets 1 chip
                players[i].isBlind = False
                players[i+1].isBlind = True

    # TODO: fix 
    # TODO: check for all-in
    # TODO: update loop for raise
    # TODO: update raise/check interaction
    # TODO: improve question line info
    def checksAndBets(self):
        for i in players:
            pot = 0
            bet = 0
            action = input(f'Player {i.playerID}: What do you want to do? (call, check, raise, fold): ')
            if action == 'fold':
                print(f'Player {i.playerID}: Folds.')
                i.isActive = False
                i.card1.state = 0
                i.card2.state = 0
                continue
            elif action == 'check':
                continue
            elif action == 'call':
                if bet == 0:    
                    bet = int(input(f'Player {i.playerID}: how much do you want to bet? '))
                    i.numChips -= bet
                    pot += bet
                else:
                    print(f'Player {i.playerID}: Called the ${bet}.')
                    i.numChips -= bet
                    pot += bet
            elif action == 'raise':
                bet = int(input(f'Player {i.playerID}: how much do you want to raise? '))
                print(f'Player {i.playerID}: Raised ${bet}.')
                i.numChips -= bet
                pot += bet
    
        print(f'the pot is now ${pot}.')
        for i in players:
            print(f'Player {i.playerID}\'s bank is now {i.numChips}.')

'''
    def checkHands():
        

    def flop():
        # TODO: flip three cards from deck
        # TODO: checks and bets
        # TODO: update pot
        # TODO: winner?

    def turn():
        # TODO: burn one card
        # TODO: flip one card
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
