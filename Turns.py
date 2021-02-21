from Player import Player
from Card import Card

Players = int(input('how many people are playing: '))
Aichips = 100
playerBank = 100
pot = 0

def turn(playerBank,label):
    action = input('do you want to check, call, raise or fold? ')
    if action == 'check':
        pass
    elif action == 'call':
        bet = int(input('how much was the original bet? '))
        playerBank -= bet
        pot += bet
    elif action == 'raise':
        bet = int(input('how much do you want to raise? '))
        pot += bet
        playerBank = playerBank - bet
    elif action == 'fold':
        Aichips += pot
    
    for k in range(Players):
        turn
