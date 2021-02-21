from Card import Card

class Player():
    def __init__(self, playerID: int, numChips: int, card1=Card('', '', 0), card2=Card('', '', 0), isBlind: int=0, isActive=True): # isBlind: 0 - no, 1 - big, 2 - small
        self.playerID = playerID
        self.numChips = numChips
        self.card1 = card1
        self.card2 = card2
        self.isBlind = isBlind
        self.isActive = isActive

    def toString(self):
        return f'{self.playerID}: {self.card1.toString()}, {self.card2.toString()} -- {self.numChips} chips'

'''
    def check():
        
    
    def fold():
        
    
    def bet():

'''
