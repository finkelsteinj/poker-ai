from Card import Card

class Player():
    def __init__(self, numChips, card1=Card('', '', 0), card2=Card('', '', 0), isBlind=False, isActive=False):
        self.numChips = numChips
        self.card1 = card1
        self.card2 = card2
        self.isBlind = isBlind
        self.isActive = isActive

'''
    def check():
        
    
    def fold():
        
    
    def bet():

'''
