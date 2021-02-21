from Card import Card
from random import shuffle 

players = []
deck    = []
suits   = ['D','H','S','C']
ids     = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
values  = [2,3,4,5,6,7,8,9,10,11,12,13,14]

for i in range(len(ids)):
    for suit in suits:
        card = Card(suit, ids[i], values[i])
        deck.append(card)

shuffle(deck)

for i in deck:
    print(i.toString())