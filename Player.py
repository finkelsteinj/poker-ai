from Card import Card

class Player():
    def __init__(self, playerID: int, numChips: int, card1=Card('', '', 0), card2=Card('', '', 0), isBlind=False, isActive=False):
        self.playerID = playerID
        self.numChips = numChips
        self.card1 = card1
        self.card2 = card2
        self.isBlind = isBlind
        self.isActive = isActive

    def toString(self):
        # print(self.name + ": " + self.card1.toString() + ", " + self.card2.toString() + f' -- {self.numChips} chips')
        print(f'{self.playerID}: {self.card1.toString()}, {self.card2.toString()} -- {self.numChips} chips')

'''
    def check():
        
    
    def fold():
        
    
    def bet():

'''
