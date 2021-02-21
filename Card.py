class Card:
    def __init__(self, suit: str, id: str, value: int, state: int = 0): # state: 0 - inactive, 1 - in hand, 2 - on table
        self.suit = suit
        self.id = id
        self.value = value
        self.state = state

    def toString(self):
        return self.id + self.suit