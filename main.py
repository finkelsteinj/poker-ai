from Poker import Poker
from Player import Player
from Card import Card

def getInputs():
    global numPlayers
    numPlayers = int(input('How many players are playing? '))

if __name__ == '__main__':
    getInputs()
    Poker(numPlayers)