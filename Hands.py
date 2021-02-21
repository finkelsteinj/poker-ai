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
                if (((players[i].card1.values[i]).intersection(flop3)) == 2 and ((players[i].card2.values).intersection(flop3) == 3)):
                    print("Full House")
                elif (((players[i].card1.values[i]).intersection(flop3)) == 3 and ((players[i].card2.values[i]).intersection(flop3) == 2)): 
                    print("Full House")
                        
            def case_5(self): #Flush
                if (players[i].card1.suits == players[i].card2.suits and 
                    
              
              
            def case_6(self):#Straight
                values = [i[0] for i in flop3]
                value_counts = defaultdict(lambda:0)
                for v in values:
                value_counts[v] += 1
                rank_values = [values[i] for i in values]
                value_range = max(values) - min(values)
                if len(set(value_counts.values())) == 1 and (value_range==4):
                    return True
                else:
                    #check straight with low Ace
                    if set(ids) == set(["A", "2", "3", "4", "5"]):
                        return True
                    return False
          
         
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
          