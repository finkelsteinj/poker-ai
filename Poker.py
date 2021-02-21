from Player import Player
from Card import Card
from Hand import Hand
from random import shuffle   

players = []
deck = []
suits = ['D','H','S','C']
ids = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
values = [2,3,4,5,6,7,8,9,10,11,12,13,14]

# initialize deck
for i in range(len(ids)):
    for suit in suits:
        card = Card(suit, ids[i], values[i])
        deck.append(card)

class Poker():

    def __init__(self, numPlayers: int=0, pot: int=0, bet: int=0):
        self.numPlayers = numPlayers
        self.pot = pot
        self.bet = bet

        self.initialDeal()
        self.preflop()
        self.flop()
    
    def checkHands(self, hand=Hand()):
        self.hand = hand
        
        for i in range(10):
            hand.checkHand(i, players[i])

    def isWinner(self):
        pass

    # TODO: check for all-in
    # TODO: improve question line info
    def checksAndBetsFunc(self, case: str, p: Player):
        def fold():
            print(f'Player {p.playerID} folds.')
            p.isActive = False
            p.card1.state = 0
            p.card2.state = 0

        def check():
            if self.bet > 0:
                print(f'Someone raised ${self.bet}.')
                action = input(f'Player {p.playerID}: What do you want to do? (call, fold, raise): ')
            else:
                pass

        def call():
            if self.bet == 0:
                self.bet = int(input(f'Player {p.playerID}: How much do you want to bet? '))
                p.numChips -= self.bet
                self.pot += self.bet
            else:
                print(f'Player {p.playerID} calls.')
                p.numChips -= self.bet
                self.pot += self.bet

        def raise2():
            self.bet = int(input(f'Player {p.playerID}: How much do you want to raise? '))
            p.numChips -= self.bet
            self.pot += self.bet
            print(f'Player {p.playerID} raises {self.bet} chips.')
        
        def default():
            print('Invalid function.')

        switcher = {
            'fold'  : fold,
            'check' : check,
            'call'  : call,
            'raise' : raise2
        }.get(case, default)()
    
    def checksAndBets(self):
        index = -1
        count = 0
        while self.bet > 0 or count < len(players):
            if players[count].isActive or self.bet > 0:
                if count == index:
                    break
                else:
                    action = input(f'Player {players[count].playerID}: What do you want to do? (fold, check, call, raise): ')
                    self.checksAndBetsFunc(action, players[count])
                    if (action == 'raise'):
                        index = players[count].playerID
            else:
                continue
            if count == len(players) - 1 and self.bet > 0:
                count = 0
            else:
                count += 1

        print(f'The pot is {self.pot} chips.')
        for i in players:
            print(f'Player {i.playerID}\'s bank is now {i.numChips} chips.')
            activeRaise = True
        print('-----------------------------------------------------')

    def initialDeal(self):
        # create players
        for i in range(self.numPlayers):
            numChips = int(input(f'How many chips is player {i} buying in for? '))
            players.append(Player(i, numChips))
        
        # deal cards
        shuffle(deck)
        count = 0
        for i in players:
            i.card1 = deck[count]
            i.card2 = deck[count+1]
            count += 2

        # output hands
        for i in range(self.numPlayers):
            print(players[i].toString())

    # TODO: assign blinds
    # TODO: update pot
    # TODO: winner?
    def preflop(self):
        '''
        for i in range(len(players)):
            if players[i] == 0:
                # big blind bets 2 chips
                # small blind bets 1 chip
                players[i].isBlind = False
                players[i+1].isBlind = True
        '''
        self.checksAndBets()

    # TODO: flip three cards from deck
    # TODO: update pot
    # TODO: winner?
    def flop(self):
        deck.append(deck[4])
        deck.pop(4)
        shuffle(deck)
        print(deck[4].toString())
        print(deck[5].toString())
        print(deck[6].toString())
        print(deck[7].toString())
        Flop1 = [deck[4].toString(), deck[5].toString(), deck[6].toString()]
        deck.append(deck[8])
        deck.pop(7)
        print(deck[7].toString())
        Flop2 = [deck[4].toString(), deck[5].toString(), deck[6].toString(), deck[7].toString()]
        deck.append(deck[8])
        deck.pop(8)
        print(deck[8].toString())
        Flop3 = [deck[4].toString(), deck[5].toString(), deck[6].toString(), deck[7].toString(), deck[8].toString()] 
        self.checksAndBets()

    def turn(self):
        pass
    
    # TODO: burn one card
    # TODO: flip another
    # TODO: checks and bets
    # TODO: update pot
    # TODO: determine winner
    # TODO: distribute pot
    def river(self):
        pass