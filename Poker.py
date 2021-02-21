from Player import Player
from Card import Card
from random import shuffle    

class Poker():

    global deck, suits, ids, values, players
    global numPlayers, numChips, pot, bet

    pot = 0
    bet = 0
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

    def __init__(self):
        shuffle(deck)
        self.initialDeal()
        self.checksAndBets()
        
    def isWinner(self):
        pass

    def initialDeal(self):
        # create players
        numPlayers = int(input('how many players are playing? '))
        for i in range(numPlayers):
            numChips = int(input(f'how many chips is player {i+1} buying in for? '))
            players.append(Player(i, numChips))
        
        # deal cards
        count = 0
        for i in players:
            i.card1 = deck[count]
            i.card2 = deck[count+1]
            count += 2
        
        # output hands
        for i in range(numPlayers):
            players[i].toString()


    # TODO: assign blinds
    # TODO: checks and bets
    # TODO: update pot
    # TODO: winner?
    def preflop(self):
        for i in range(len(players)):
            if players[i].isBlind:
                # big blind bets 2 chips
                # small blind bets 1 chip
                players[i].isBlind = False
                players[i+1].isBlind = True

    # TODO: check for all-in
    # TODO: update loop for raise
    # TODO: update raise/check interaction
    # TODO: improve question line info
    def checksAndBetsFunc(self, case: str, p: Player):
        self.case = case
        self.p = p
        activeRaise = False

        global pot, bet

        def fold():
            print(f'Player {p.playerID} folds.')
            p.isActive = False
            p.card1.state = 0
            p.card2.state = 0

        def check():
            if bet > 0:
                print(f'Someone raised ${bet}.')
                action = input(f'Player {p.playerID}: What do you want to do? (call, fold, raise): ')
            else:
                pass

        def call():
            if bet == 0:
                self.bet = int(input(f'Player {p.playerID}: How much do you want to bet? '))
                p.numChips -= bet
                pot += bet
            else:
                print(f'Player {p.playerID} calls.')
                p.numChips -= bet
                pot += bet

        def raise2():
            bet = int(input(f'Player {p.playerID}: how much do you want to raise? '))
            print(f'Player {p.playerID} raises ${bet}.')
            p.numChips -= bet
            pot += bet
#            activeRaise = True

        def default():
            print('Invalid function.')

        switcher = {
            'fold'  : fold,
            'check' : check,
            'call'  : call,
            'raise' : raise2,
        }

        if activeRaise:
            while activeRaise:
                switcher.get(case, default)()
        else:
            switcher.get(case, default)()

    def checksAndBets(self):
        for i in players:
            action = input(f'Player {i.playerID}: What do you want to do? (call, check, fold, raise): ')
            self.checksAndBetsFunc(action, i)

    '''
    def checksAndBets(self):
        j = 0
        while j < len(players):
            i = players[j]
            pot = 0
            bet = 0
            temp = 0
            action = input(f'Player {i.playerID}: What do you want to do? (call, check, fold, raise): ')
            if action == 'fold':
                print(f'Player {i.playerID} folds.')
                i.isActive = False
                i.card1.state = 0
                i.card2.state = 0
                continue
            elif action == 'check':
                condition = True
                while condition:
                    if bet > 0:
                        print(f'Someone raised ${bet}.')
                        action = input(f'Player {i.playerID}: What do you want to do? (call, fold, raise): ')
                    else:
                        condition = False
            elif action == 'call':
                if bet == 0:    
                    bet = int(input(f'Player {i.playerID}: how much do you want to bet? '))
                    i.numChips -= bet
                    pot += bet
                else:
                    print(f'Player {i.playerID} calls')
                    i.numChips -= bet
                    pot += bet
            elif action == 'raise':
                bet = int(input(f'Player {i.playerID}: how much do you want to raise? '))
                print(f'Player {i.playerID} raises ${bet}.')
                i.numChips -= bet
                pot += bet
            j += 1

        print(f'The pot is now ${pot}.')
        for i in players:
            print(f'Player {i.playerID}\'s bank is now ${i.numChips}.')
        print('-----------------------------------------------------')
'''

'''
    def checkHands(self):
        

    def flop(self):
        # TODO: flip three cards from deck
        # TODO: checks and bets
        # TODO: update pot
        # TODO: winner?

    def turn(self):
        # TODO: burn one card
        # TODO: flip one card
        # TODO: checks and bets
        # TODO: update pot
        # TODO: winner?

    def river(self):
        # TODO: burn one card
        # TODO: flip another
        # TODO: checks and bets
        # TODO: update pot
        # TODO: determine winner
        # TODO: distribute pot
        
'''
