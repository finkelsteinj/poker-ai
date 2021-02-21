from Player import Player
from Card import Card
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
            if count == len(players) - 1:
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
            players[i].toString()

    # TODO: assign blinds
    # TODO: checks and bets
    # TODO: update s
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
    # TODO: checks and bets
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
        Flop1 = list(deck[4].toString(), deck[5].toString(), deck[6].toString())
        deck.append(deck[8])
        deck.pop(7)
        print(deck[7].toString())
        Flop2 = list(deck[4].toString(), deck[5].toString(), deck[6].toString(), deck[7].toString())
        deck.append(deck[8])
        deck.pop(8)
        print(deck[8].toString())
        Flop3 = list(deck[4].toString(), deck[5].toString(), deck[6].toString(), deck[7].toString(), deck[8].toString())
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

'''
    def checkHands():
        class PythonSwitchStatement:
        #Syntax most likely wrong but the ".ssubset" and ".intersection" method is the 
        #most useful method for comparing hands to the blind
        #sorry if I mixed C++ with Python 
        #but the concepts for each hand type should be correct
        #determining winner still needs to be done
        # my thought was to use the string printed out and compare 
        #the two players and whichever has the higher ranking
        #string will be given the isWinner and acquires the pot
            def switch(self, cards):
                default = "Impossible Hand"
                return getattr(self, 'case_' + str(suits) + int(values), lambda: default)()
      
            def case_1(self):#Royal Flush
                RFlush = list (card(suits[j], values[10]), card(suits[j], values[11]), card(suits[j], values[12]), card(suits[j], values[13]), card(suits[j], values[14]))
                if  (card.suits[j] == flop3):
                    flop3.append(Hand)
                    if flop3.issubset(RFlush) == True:
                    print("Royal Flush")
                    players[i] = isWinner()
                  
            def case_2(self): #Straight Flush
                if (card.suits[j] == flop3):
                    Combi = flop3.append(Hand)
                if flop3.issubset(Flush):
                    print("Straight Flush")
                                
            def case_3(self): #Four of a kind
                if (((players[i].card1.values[i]).intersection(flop3)) == 2 and ((players[i].card2.values[i]).intersection(flop3) == 2)):
                    print("Four of a kind")
          
            def case_4(self): #Full House
                if (((players[i].card1.values[i]).intersection(flop3)) == 2 and ((players[i].card2.values).intersection(flop3) == 3)):
                    print("Full House")
                elif (((players[i].card1.values[i]).intersection(flop3)) == 3 and ((players[i].card2.values[i]).intersection(flop3) == 2)): 
                    print("Full House")
                        
            def case_5(self): #Flush
                if (players[i].card1.suits == players[i].card2.suits and True):
                    pass
                    
            def case_6(self): #Straight
                pass
                    
            def case_7(self): #Three of a kind
                if ((((players[i].card1.values[i]).intersection(flop3)) == 3 and ((players[i].card2.values).intersection(flop3) != 2)) or ((players[i].card1.values[i]).intersection(flop3)) != 2 and ((players[i].card2.values).intersection(flop3) == 3))):
                    print("Three of a kind")
                    
            def case_8(self): #Two Pair
                if ((((players[i].card1.values[i]).intersection(flop3)) == 2 and ((players[i].card2.values).intersection(flop3) != 3)) or ((players[i].card1.values[i]).intersection(flop3)) != 3 and ((players[i].card2.values).intersection(flop3) == 2))):
                    print("Two pair")
            
            def case_9(self): #One Pair
                if players[i].card1.values[i] == 1 or players[i].card2.values[i] == 1:
                    print("One Pair")
            
            def case_10(self): #High Card
                if Hand != flop3:
                    if players[i].card1.values[i] > players[i].card2.values[i]:
                        print('High card card1')
                    else:
                        print('High card card2')
    '''      
