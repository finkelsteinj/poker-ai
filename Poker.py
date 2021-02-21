from Card import Card
from Player import Player

from random import shuffle    

deck   = []
suits  = ['D', 'H', 'S', 'C']
ids    = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14']

for i in range(len(ids)):
    for j in range(len(suits)):
        card = Card(suits[j], ids[i], values[i])
        deck.append(card)

for i in range(len(deck)):
    print(deck[i].id + deck[i].suit)


