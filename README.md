# Blackjack-in-Python
The game of blackjack implemented in Python.

* Deck:\
         A deck is represented by a list of tuples.\
         Each tuple takes a rank from a list of ranks and a suit from a list of suits.\
         <pre>
                  ex. deck = [('A', 'Clubs'), ('2', 'Hearts'), ...]
         </pre>
         The game has 4 decks, so after we make one deck we multiply it by 4 and then shuffle them (random.shuffle(self.four_decks)).

* How to play:\
         Choose Play option from the start menu.\
         First, the game asks you to enter your bankroll (ex. 1000) and then to bet an amount for the next hand.\
         Betting options are bills of 10, 25, 50 and 100 with a limit on 1000 per hand.\
         This game supports Hit, Stand, Double Down and Split actions for the player.\
         After a hand, the game determines the winner and gives the reward or takes the bet from the player.

<pre>
1) Play
2) Print rules
3) Exit
Choose an option: 1

********************GAME SETUP********************
Shuffling...
Decks are ready.
Give your bankroll: 1000
Player sat on table

********************GAME STARTED********************
-----------------------------------------
         Place your bets...
-----------------------------------------
Bet:  0
Balance:  1000
Options: 1)10, 2)25, 3)50, 4)100, 5)Deal
4
Bet:  100
Balance:  900
Options: 1)10, 2)25, 3)50, 4)100, 5)Deal
5
-----------------------------------------
         Dealing...
-----------------------------------------
>Dealer: 
      ('4', 'Diamonds')
     total:  4
>Player: 
      ('3', 'Hearts')
      ('3', 'Diamonds')
     total:  6
-----------------------------------------
         Play...
-----------------------------------------
>Player: 
Options: H, S, D, SP: 
H
      ('3', 'Hearts')
      ('3', 'Diamonds')
      ('5', 'Spades')
     total:  11
Options: H, S, D, SP: 
H
      ('3', 'Hearts')
      ('3', 'Diamonds')
      ('5', 'Spades')
      ('4', 'Clubs')
     total:  15
Options: H, S, D, SP: 
H
      ('3', 'Hearts')
      ('3', 'Diamonds')
      ('5', 'Spades')
      ('4', 'Clubs')
      ('8', 'Clubs')
     total:  23
Busted!
>Dealer: 
      ('4', 'Diamonds')
      ('A', 'Hearts')
     total:  15
-----------------------------------------
Dealer wins!
New balance:  900
-----------------------------------------
</pre>

* Classes:
  
  Game: Where the game takes place.\
  **handSetup()\
  **hit()\
  **play()\
  **evaluate()
 
  Player: The player who sits on table.\
  **bet()\
  **calculateValue()\
  **printCards()\
  **printCurrValue()

  Dealer: The dealer who deals the cards.\
  **calculateValue()\
  **printCards()\
  **printCurrValue()
