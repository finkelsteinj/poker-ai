from Player import Player
from Card import Card

class Hand:
    def __init__(self, card1=Card('', '', 0), card2=Card('', '', 0), handOnTable=[]):
        self.card1 = card1
        self.card2 = card2
        self.handOnTable = handOnTable

    def checkHand(self, case: int=-1, player=Player(0, 0)):
        def royalFlush(self, player):
            RFlush = list (self.card.suit, values[10]), self.card.suit, values[11], self.card.suit, values[12], self.card.suit, values[13], self.card.suit, values[14]
            if  (self.card.suit == flop3):
                flop3.append(Hand)
            if flop3.issubset(RFlush) == True:
                print("Royal Flush")
        
        def straightFlush(self, player):
            if (self.card.suit == flop3):
                Combi = flop3.append(Hand)
            if flop3.issubset(Combi):
                print("Straight Flush")
                    
        def fourKind(self, player):
            if (((self.card1.values).intersection(flop3)) == 2 and ((self.card2.values).intersection(flop3) == 2)):
                print("Four of a kind")

        def fullHouse(self, player):
            if (((self.card1.values).intersection(flop3)) == 2 and ((self.card2.values).intersection(flop3) == 3)):
                print("Full House")
            elif (((self.card1.values).intersection(flop3)) == 3 and ((self.card2.values).intersection(flop3) == 2)): 
                print("Full House")
            
        def flush(self, player):
            if (self.card1.suit == players.card2.suits and True):
                pass
        
        def straight(self, player):
            pass

        def threeKind(self, player):
            if ((self.card1.values).intersection(flop3)) == 3 and ((self.card2.values).intersection(flop3) != 2) or ((self.card1.values).intersection(flop3)) != 2 and (((self.card2.values).intersection(flop3) == 3)):
                print("Three of a kind")
        
        def twoPair(self, player):
            if ((self.card1.values).intersection(flop3)) == 2 and ((self.card2.values).intersection(flop3) != 3) or ((self.card1.values).intersection(flop3)) != 3 and ((self.card2).intersection(flop3) == 2):
                print("Two pair")

        def onePair(self, player):
            if self.card1.values == 1 or self.card2.values == 1:
                print("One Pair")

        def highCard(self, player):
            if Hand != flop3:
                if self.card1.values > self.card2.values:
                    print('High card ''players.card1.values')
                else:
                    print('High card ''players.card2.values')
        
        switcher = {
            0 : royalFlush(i),
            1 : straightFlush(i),
            2 : fourKind(i),
            3 : fullHouse(i),
            4 : flush(i),
            5 : straight(i),
            6 : threeKind(i),
            7 : twoPair(i),
            8 : onePair(i),
            9 : highCard(i)
        }.get(case)