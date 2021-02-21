class Card:
    def __init__(self, suit: str, id: str, value: int, isInHand=False, isOnTable=False):
        self.suit = suit
        self.id = id
        self.value = value
        self.isInHand = isInHand
        self.isOnTable = isOnTable

    def toString(self):
        return self.id + self.suit

'''
    def shuffle():


    def deal():

'''