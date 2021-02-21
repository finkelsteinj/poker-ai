
  
"""
Created on Sun Feb 21 04:48:38 2021

@author: jared
"""

  
from Player import Player
from Card import Card
from random import shuffle    

class Poker():

    global deck, suits, ids, values, players
    global numPlayers, numChips
    
    players = []
    deck = []
    suits = ['D','H','S','C']
    ids = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
    values = [2,3,4,5,6,7,8,9,10,11,12,13,14]

    # initialize deck
    for i in range(len(ids)):
        for j in range(len(suits)):
            card = Card(suits[j], ids[i], values[i])
            deck.append(card)

    def __init__(self):
        shuffle(deck)
        self.initialDeal()
        self.checksAndBets()
        
    def isWinner():
        pass

    def initialDeal(self):
        # create players
        numPlayers = int(input('how many players are playing? '))
        for i in range(numPlayers):
            numChips = int(input(f'how many chips is player {i+1} buying in for? '))
            players.append(Player(i, numChips))
        
        # deal cards
        count = 0
        for i in range(numPlayers):
            players[i].card1 = deck[count]
            players[i].card2 = deck[count+1]
            count += 2
        
        for i in range(numPlayers):
            players[i].toString()

    def preflop(self):
        # TODO: assign blinds
        # TODO: checks and bets
        # TODO: update pot
        # TODO: winner?

        for i in range(len(players)):
            if players[i].isBlind:
                # big blind bets 2 chips
                # small blind bets 1 chip
                players[i].isBlind = False
                players[i+1].isBlind = True

    # TODO: fix 
    # TODO: check for all-in
    # TODO: update loop for raise
    # TODO: update raise/check interaction
    # TODO: improve question line info
    def checksAndBets(self):
        for i in players:
            pot = 0
            bet = 0
            action = input(f'Player {i.playerID}: What do you want to do? (call, check, raise, fold): ')
            if action == 'fold':
                print(f'Player {i.playerID}: Folds.')
                i.isActive = False
                i.card1.state = 0
                i.card2.state = 0
                continue
            elif action == 'check':
                continue
            elif action == 'call':
                if bet == 0:    
                    bet = int(input(f'Player {i.playerID}: how much do you want to bet? '))
                    i.numChips -= bet
                    pot += bet
                else:
                    print(f'Player {i.playerID}: Called the ${bet}.')
                    i.numChips -= bet
                    pot += bet
            elif action == 'raise':
                bet = int(input(f'Player {i.playerID}: how much do you want to raise? '))
                print(f'Player {i.playerID}: Raised ${bet}.')
                i.numChips -= bet
                pot += bet
    
        print(f'the pot is now ${pot}.')
        for i in players:
            print(f'Player {i.playerID}\'s bank is now {i.numChips}.')
            def flop():
        # TODO: flip three cards from deck
                deck.append(deck[4])
                deck.pop(4)
                shuffle(deck)
                print(deck[4].toString())
                print(deck[5].toString())
                print(deck[6].toString())
                print(deck[7].toString())
                Flop1 = list(deck[4].toString(), deck[5].toString(), deck[6].toString())
                deck.append(deck[8])
                deck.pop(7)
                print(deck[7].toString())
                Flop2 = list(deck[4].toString(), deck[5].toString(), deck[6].toString(), deck[7].toString())
                deck.append(deck[8])
                deck.pop(8)
                print(deck[8].toString())
                Flop3 = list(deck[4].toString(), deck[5].toString(), deck[6].toString(), deck[7].toString(), deck[8].toString())

    def checkHands():
        class PythonSwitchStatement:
    #Syntax most likely wrong but the ".ssubset" and ".intersection" method is the 
    #most useful method for comparing hands to the blind
    #sorry if I mixed C++ with Python 
    #but the concepts for each hand type should be correct
    #determining winner still needs to be done
    # my thought was to use the string printed out and compare 
    #the two players and whichever has the higher ranking
    #string will be given the isWinner and acquires the pot
            def switch(self, cards):
                default = "Impossible Hand"
                return getattr(self, 'case_' + str(suits) + int(values), lambda: default)()
      
            def case_1(self):#Royal Flush
                RFlush = list (card(suits[j], values[10]), card(suits[j], values[11]), card(suits[j], values[12]), card(suits[j], values[13]), card(suits[j], values[14]))
                if  (card.suits[j] == flop3):
                  flop3.append(Hand)
                  if flop3.issubset(RFlush) == True:
                      print("Royal Flush")
                  players[i] = isWinner()
                  
                  def case_2(self): #Straight Flush
                      if (card.suits[j] == flop3):
                          Combi = flop3.append(Hand)
                          if flop3.issubset(Flush):
                              print("Straight Flush")
                                
                              def case_3(self): #Four of a kind
                                  if (((players[i].card1.values[i]).intersection(flop3)) == 2 and ((players[i].card2.values[i]).intersection(flop3) == 2)):
                                      print("Four of a kind")
          
                                      def case_4(self): #Full House
                                          if (((players[i].card1.values[i]).intersection(flop3)) == 2 and ((players[i].card2.values).intersection(flop3) == 3))
                                              print("Full House")
                                                  else if (((players[i].card1.values[i]).intersection(flop3)) == 3 and ((players[i].card2.values[i]).intersection(flop3) == 2)): 
                                                      print("Full House")
                        
      def case_5(self): #Flush
          if (players[i].card1.suits == players[i].card2.suits and 
              
              
      def case_6(self): #Straight
          if 
          
         
      def case_7(self): #Three of a kind
          if (((players[i].card1.values[i]).intersection(flop3)) == 3 and ((players[i].card2.values).intersection(flop3) != 2)) || ((players[i].card1.values[i]).intersection(flop3)) != 2 
              and ((players[i].card2.values).intersection(flop3) == 3))
              print("Three of a kind")
              
      def case_8(self): #Two Pair
          if (((players[i].card1.values[i]).intersection(flop3)) == 2 and ((players[i].card2.values).intersection(flop3) != 3)) || ((players[i].card1.values[i]).intersection(flop3)) != 3 
              and ((players[i].card2.values).intersection(flop3) == 2))
                print("Two pair")
      def case_9(self): #One Pair
          if players{i}.card1.values[i] == 1 || players[i].card2.values[i] == 1:
              print("One Pair")
      def case_10(self): #High Card
          if Hand[] != flop3:
              if players{i}.card1.values[i] > players[i].card2.values[i]:
                  print ('High card card1')
                  else 
                      print('High card card2')
          
        
      
             
            '''
        # TODO: checks and bets
        # TODO: update pot
        # TODO: winner?
    def turn():
        # TODO: burn one card
        # TODO: flip one card
        # TODO: checks and bets
        # TODO: update pot
        # TODO: winner?

        
'''
