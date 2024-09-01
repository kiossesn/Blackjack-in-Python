import random
import time

ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']


class Game:
    def __init__(self):
        print()
        print("********************GAME SETUP********************")
        # Step 1: Create a single deck of cards
        deck = []
        for suit in suits:
            for rank in ranks:
                deck.append((rank, suit))

        # Step 2: Create four decks (concatenate four copies of the deck)
        self.four_decks = deck * 4  # This creates a list with 4 copies of the deck

        print("Shuffling...")
        time.sleep(2)

        # Step 3: Shuffle the combined deck
        random.shuffle(self.four_decks)
        print("Decks are ready.")

        # New dealer
        self.dealer = Dealer()

        # New player
        bankroll = int(input("Give your bankroll: "))
        self.player = Player(bankroll)
        print("Player sat on table")

    def play(self):
        print()
        print("********************GAME STARTED********************")
        while (True):
            # This flag becomes true if player or dealer has a Blackjack
            f = False

            # Betting
            print("-----------------------------------------")
            print("         Place your bets...")
            print("-----------------------------------------")
            bet = self.player.bet()

            # Hand setup
            print("-----------------------------------------")
            print("         Dealing...")
            print("-----------------------------------------")
            self.handSetup()

            print(">Dealer: ")
            # Print dealer's first card
            self.dealer.printCards(1)
            # Calculate and print dealer's first card's value
            self.dealer.calculateValue(1)

            print(">Player: ")
            # Print player's cards
            self.player.printCards()
            # Calculate and print player's cards value
            self.player.calculateValue()

            # Keywords:
            #           'bj' : player/dealer has a blackjack
            #           'bust' : player/dealer busts
            #           '21 : player/dealer hits 21
            #           'continue' : none of the above
            dout = "continue"
            pout = "continue"

            # Dealer has a blackjack
            if self.dealer.currValue == 21:
                self.evaluate('L', bet)
                dout = 'bj'
                f = True
            # Player has a blackjack
            if self.player.currValue == 21:
                self.evaluate('BJ', bet)
                pout = 'bj'
                f = True

            if f == False:
                # Play
                print("-----------------------------------------")
                print("         Play...")
                print("-----------------------------------------")

                # This flag determines if it's time for dealer to play
                flag = False

                # Player's turn
                print(">Player: ")
                while(True):
                    print("Options: H, S, D, SP: ")
                    option = input()

                    if option == 'H':
                        # Player hits
                        pout = self.hit(self.player)

                        # Player busts
                        if pout == 'bust':
                            print("Busted!")
                            time.sleep(1)

                            print(">Dealer: ")

                            # Reveal dealer's both cards and total value
                            self.dealer.printCards(3)
                            self.dealer.printCurrValue()

                            # Player loosing routine
                            self.evaluate('L', bet)
                            break

                        # Player hits 21 => exit loop
                        elif pout == '21':
                            flag = True
                            break

                        else:
                            continue

                    # Exit loop with Stand command
                    elif option == 'S':
                        flag = True
                        break

                # Dealer's turn
                if flag == True:

                    print(">Dealer: ")

                    # Reveal both dealer's cards and total value
                    self.dealer.printCards(3)
                    self.dealer.printCurrValue()

                    while(True):
                        # Dealer hits bellow 17
                        if self.dealer.currValue < 17:
                            time.sleep(1)
                            print('Hit')
                            dout = self.hit(self.dealer)

                            # Dealer busts
                            if dout == 'bust':
                                print("Busted!")
                                time.sleep(1)

                                # Player winning routine
                                self.evaluate('W', bet)
                                break

                        # Dealer stands
                        else:
                            print('Stand')
                            time.sleep(1)
                            break

            # Determine winner if nobody busted and nobody has a blackjack
            if pout != 'bust' and dout != 'bust' and pout != 'bj' and dout != 'bj':
                if self.player.currValue > self.dealer.currValue:
                    self.evaluate('W', bet)
                elif self.dealer.currValue > self.player.currValue:
                    self.evaluate('L', bet)
                else:
                    self.evaluate('P', bet)

            # Continue?
            print()
            op = input("Press enter to continue, or 'E' to exit...")
            if op == 'E':
                break
            else:
                print()
                continue

    def handSetup(self):
        # Clear player's list of cards
        self.player.cards.clear()
        # Draw two cards for the player and remove them from the deck
        p1 = self.four_decks.pop(0)
        self.player.cards.append(p1)
        p2 = self.four_decks.pop(0)
        self.player.cards.append(p2)

        # Clear dealer's list of cards
        self.dealer.cards.clear()
        # Draw two cards for the dealer and remove them from the deck
        d1 = self.four_decks.pop(0)
        self.dealer.cards.append(d1)
        d2 = self.four_decks.pop(0)
        self.dealer.cards.append(d2)

    def hit(self, guy):
        """
        Perform the hit action.
        :param guy: player or dealer
        :return: 'bust' if the guy busted or 'continue' if he didn't or '21' if guy hits 21
        """
        if guy == self.player:
            # Print player's cards
            guy.printCards()
        else:
            # Print dealer's cards
            guy.printCards(2)

        time.sleep(1)

        # Draw a card and remove it from the deck
        card = self.four_decks.pop(0)
        # Add the card to player's cards
        guy.cards.append(card)
        # Print the new card above the others
        print("     ", card)

        if guy == self.player:
            # Calculate and print the new total value of the cards
            guy.calculateValue()
        else:
            # Calculate and print the new total value of the cards
            guy.calculateValue(2)

        time.sleep(1)

        # 21
        if guy.currValue == 21:
            return '21'

        # Bust
        if guy.currValue > 21:
            return 'bust'
        else:
            return 'continue'

    def evaluate(self, res, bet):
        """
        Changes the player's balance depending on the outcome of the hand.
        :param res: 'W' : player wins, 'BJ' : player wins with a blackjack, 'L' : player looses, 'P' : push
        :param bet: player's bet on the particular hand
        """
        print("-----------------------------------------")
        if res == 'W':
            print("Player wins!")
            self.player.remaining = self.player.remaining + bet
            print("New balance: ", self.player.remaining)
        if res == 'BJ':
            print("Player blackjack!")
            self.player.remaining = self.player.remaining + bet + bet * 1 / 2
            print("New balance: ", self.player.remaining)
        if res == 'L':
            print("Dealer wins!")
            self.player.remaining = self.player.remaining - bet
            print("New balance: ", self.player.remaining)
        if res == 'P':
            print("It's a push.")
            self.player.remaining = self.player.remaining + 0
            print("New balance: ", self.player.remaining)
        print("-----------------------------------------")


class Player:
    def __init__(self, remaining):
        # Keeps the balance - the remaining money for the player
        self.remaining = remaining
        # Keeps the player's dealt cards for a hand
        self.cards = []
        # Keeps the total value of the player's dealt cards for a hand
        self.currValue = 0

    def bet(self):
        bet = 0
        rem = self.remaining
        while(True):
            print("Bet: ", bet)
            print("Balance: ", rem)
            print("Options: 1)10, 2)25, 3)50, 4)100, 5)Deal")
            option = input()

            if option == '1':
                if rem >= 10:
                    bet += 10
                    rem -= 10
                elif rem < 10:
                    print("!You do not have enough money, try again!")
            elif option == '2':
                if rem >= 25:
                    bet += 25
                    rem -= 25
                elif rem < 25:
                    print("!You do not have enough money, try again!")
            elif option == '3':
                if rem >= 50:
                    bet += 50
                    rem -= 50
                elif rem < 50:
                    print("!You do not have enough money, try again!")
            elif option == '4':
                if rem >= 100:
                    bet += 100
                    rem -= 100
                elif rem < 100:
                    print("!You do not have enough money, try again!")
            elif option == '5':
                if bet == 0:
                    print("!No bet added, try again!")
                    continue
                break
            else:
                print("!Wrong input, try again!")

            if bet > 1000:
                print("!Maximum bet is 1000$, try again!")
                rem += bet
                bet = 0
        return bet

    def calculateValue(self):
        value = 0

        # Iterate through all the player's cards and calculate the total value

        # This flag becomes true if 'A' counts for 11
        flag = False

        for card in self.cards:
            if card[0] == 'J' or card[0] == 'Q' or card[0] == 'K' or card[0] == '10':
                value += 10
            elif card[0] == 'A':
                if value + 11 > 21:
                    value += 1
                else:
                    value += 11
                    flag = True
            else:
                value += int(card[0])

        # If value is over 21 and there is an 'A' that counts as 11, count it as 1
        if value > 21 and flag == True:
            value -= 10

        # Update currValue
        self.currValue = value

        # Print the total value
        self.printCurrValue()

        return value

    def printCards(self):
        for card in self.cards:
            print("     ", card)

    def printCurrValue(self):
        print("     total: ", self.currValue)


class Dealer:
    def __init__(self):
        # Keeps the dealer's dealt cards for a hand
        self.cards = []
        # Keeps the total value of the dealer's dealt cards for a hand
        self. currValue = 0

    def calculateValue(self, mode):
        """
        :param mode: Mode 1 prints only the value of the first card but calculates the total value of all the cards (Hand setup)
                     Mode 2 calculates and prints the total value of all the cards
        :return: the total value of the cards
        """
        value = 0

        # Mode 1: Hand start
        if mode == 1:
            # First card is a 10
            if self.cards[0][0] == 'J' or self.cards[0][0] == 'Q' or self.cards[0][0] == 'K' or self.cards[0][0] == '10':
                print("Checking for Blackjack...")
                time.sleep(1)

                # Second card is an 'A'
                if self.cards[1][0] == 'A':
                    print("     ", self.cards[1])
                    print("Blackjack!")
                    time.sleep(1)
                else:
                    print("     total: ", 10)
                    time.sleep(1)

            # First card is an 'A'
            elif self.cards[0][0] == 'A':
                print("Checking for Blackjack...")
                time.sleep(1)

                # Second card is a 10
                if self.cards[1][0] == 'Q' or self.cards[1][0] == 'J' or self.cards[1][0] == 'K' or self.cards[1][0] == '10':
                    print("     ", self.cards[1])
                    print("Blackjack!")
                    time.sleep(1)
                else:
                    print("     total: 1/11")
                    time.sleep(1)

            else:
                print("     total: ", int(self.cards[0][0]))

        # Mode 1 and 2: Iterate through all the dealer's cards and calculate the total value

        # This flag becomes true if 'A' counts for 11
        flag = False

        for card in self.cards:
            if card[0] == 'J' or card[0] == 'Q' or card[0] == 'K' or card[0] == '10':
                value += 10
            elif card[0] == 'A':
                if value + 11 > 21:
                    value += 1
                else:
                    value += 11
                    flag = True
            else:
                value += int(card[0])

        # If value is over 21 and there is an 'A' that counts as 11, count it as 1
        if value > 21 and flag == True:
            value -= 10

        # Update currValue
        self.currValue = value

        # Print the total value only in mode 2
        if mode == 2:
            self.printCurrValue()

        return value

    def printCards(self, mode):
        """
        :param mode: Mode 1 prints only the first card (Hand setup)
                     Mode 2 prints all the cards
                     Mode 3 prints all the cards with a delay between them (Reveal first two cards)
        """
        if mode == 1:
            print("     ", self.cards[0])
        elif mode == 2:
            for card in self.cards:
                print("     ", card)
        elif mode == 3:
            for card in self.cards:
                print("     ", card)
                time.sleep(1)

    def printCurrValue(self):
        print("     total: ", self.currValue)


def printRules():
    print()
    print("********************GAME RULES********************")
    print("Game has 4 decks")
    print("Blackjack pays 3 to 2")
    print("Dealer stays on all 17s")
    print("Min bet: 10$")
    print("Max bet: 1000$")


# main
print("1) Play")
print("2) Print rules")
print("3) Exit")
option = input("Choose an option: ")
if option == '1':
    game = Game()
    game.play()
elif option == '2':
    printRules()
else:
    exit(0)
