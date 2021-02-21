"""
Created on Sat Feb 20 22:36:43 2021

@author: jared
"""
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

    # TODO: check for all-in
    # TODO: update loop for raise
    # TODO: update raise/check interaction
    # TODO: improve question line info
    def checksAndBetsFunc(self, case: str, p: Player):
        self.case = case
        self.p = p
        
        global pot, bet
        activeRaise = False

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
            bet = int(input(f'Player {p.playerID}: How much do you want to raise? '))
            print(f'Player {p.playerID} raises ${bet}.')
            p.numChips -= bet
            pot += bet
        
        def default(self):
            print('Invalid function.')

        switcher = {
            'fold'  : fold,
            'check' : check,
            'call'  : call,
            'raise' : raise2
        }
        
        switcher.get(case, default)
    
    def checksAndBets(self):
        for i in players:
            action = input(f'Player {i.playerID}: What do you want to do? (fold, check, call, raise): ')
            self.checksAndBetsFunc(action, i)

        print(f'The pot is ${pot}.')
        for i in players:
            print(f'Player {i.playerID}\'s bank is now ${i.numChips}.')
            activeRaise = True
        print('-----------------------------------------------------')

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

    # TODO: flip three cards from deck
    # TODO: checks and bets
    # TODO: update pot
    # TODO: winner?
    def flop(self):
        
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
flop3 = list(deck[4].toString(), deck[5].toString(), deck[6].toString(), deck[7].toString(), deck[8].toString())

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
       
           for i in players:
                 def switch(self, cards):
                    default = "Impossible Hand"
                    return getattr(self, 'case_' + str(self.card.suit) + int(values), lambda: default)()
      
                    def case_1(self):#Royal Flush
                        RFlush = list (self.card.suit, values[10]), self.card.suit, values[11], self.card.suit, values[12], self.card.suit, values[13], self.card.suit, values[14]
                        if  (self.card.suit == flop3):
                            flop3.append(Hand)
                    if flop3.issubset(RFlush) == True:
                        print("Royal Flush")
                    
                  
                    def case_2(self): #Straight Flush
                        if (self.card.suit == flop3):
                            Combi = flop3.append(Hand)
                    if flop3.issubset(Combi):
                        print("Straight Flush")
                                
                        def case_3(self): #Four of a kind
                            if (((self.card1.values).intersection(flop3)) == 2 and ((self.card2.values).intersection(flop3) == 2)):
                                print("Four of a kind")
          
                    def case_4(self): #Full House
                        if (((self.card1.values).intersection(flop3)) == 2 and ((self.card2.values).intersection(flop3) == 3)):
                            print("Full House")
                        elif (((self.card1.values).intersection(flop3)) == 3 and ((self.card2.values).intersection(flop3) == 2)): 
                            print("Full House")
                        
                        def case_5(self): #Flush
                            if (self.card1.suit == players.card2.suits and True):
                                pass
                    
                       def case_6(self): #Straight
                            values = [i[0] for i in Flop3]
                            value_counts = deck(lambda:0)
                            for v in values:
                            value_counts[v] += 1
                            rank_values = [values[i] for i in values]
                            value_range = max(values) - min(values)
                            if len(set(value_counts.values())) == 1 and (value_range==4):
                                return True
                            else:
                            #check straight with low Ace
                            if set(ids) == set(["A", "2", "3", "4", "5"]):
                                return True
                            return False

                            def case_7(self): #Three of a kind
                                if ((self.card1.values).intersection(flop3)) == 3 and ((self.card2.values).intersection(flop3) != 2) or ((self.card1.values).intersection(flop3)) != 2 and (((self.card2.values).intersection(flop3) == 3)):
                                    print("Three of a kind")
                    
                    def case_8(self): #Two Pair
                        if ((self.card1.values).intersection(flop3)) == 2 and ((self.card2.values).intersection(flop3) != 3) or ((self.card1.values).intersection(flop3)) != 3 and ((self.card2).intersection(flop3) == 2):
                            print("Two pair")
            
                    def case_9(self): #One Pair
                        if self.card1.values == 1 or self.card2.values == 1:
                            print("One Pair")
            
                        def case_10(self): #High Card
                            if Hand != flop3:
                                if self.card1.values > self.card2.values:
                                    print('High card ''players.card1.values')
                                else:
                                            print('High card ''players.card2.values')
      
