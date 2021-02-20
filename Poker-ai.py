"""
Created on Sat Feb 20 13:48:36 2021

@author: James
"""

from random import shuffle    

deck = []
suits = ['D', 'H', 'S', 'C']

nums = ['2','3','4','5','6','7','8','9','10','11','12','13','14']

for n in nums:
    for s in suits:
        card = Card(s, n)
        deck.append(card)


shuffle(deck)

for i in range(len(deck)):
    print(deck[i].num + deck[i].suit)
