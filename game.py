#this is the hilo game
import random as r
import time
import sys

def typingPrint(text):
  for character in text:
    sys.stdout.write(character)
    sys.stdout.flush()
    time.sleep(0.03)

player_points = int(300)


class PlayerPoints:
    def __init__(self):
        self.points = 300

    def add(self):
        self.points += 100
    
    def subtract(self):
        self.points -= 75

player_points_int = PlayerPoints()


typingPrint("Welcome to hilo!")
print()
print()
rules = input("Do you know how to play? Type 'y' for yes and 'n' for no: ")
if rules == 'n':
    print()
    typingPrint("Here's how to play:")
    print()
    typingPrint("You start with 300 points. I will display a card number. Your objective is to guess if the next card I draw is more or less than the card displayed on the screen. If you guess correctly, you get 100 points! If you guess incorrectly, you lose 75 points. To guess higher or lower when prompted, enter in either 'h' for higher or 'l' for lower.")
    print()
print()
typingPrint("Have fun!")
print()
print()
time.sleep(2)

def card_guesses(player_points):
    continue_playing = "y"
    
    while continue_playing == "y":
        card_number = r.randint(1,13)
        next_card = r.randint(1,13)
    
        typingPrint(f"The current card is {card_number}")
        print()
        low_or_high = input("Is the next card higher or lower?: ")
        print()

        #if the player guesses higher
        if low_or_high == "h":
            low_or_high = card_number
            typingPrint("You guessed 'higher'")
            print()

            if low_or_high < next_card:
                typingPrint("Answer in:")
                time.sleep(1)
                print()
                print("3...")
                time.sleep(1)
                print("2...")
                time.sleep(1)
                print("1...")
                time.sleep(1)
                typingPrint(f"The next card was {next_card}")
                print()
                # if the player guesses higher and the next card is higher than the old card 
                #player_points += int(100)
                player_points.add()

                typingPrint(f"That is correct! You now have {player_points} points.")
                print()

            elif low_or_high > next_card:
                #if the player guesses higher and the next card is lesser than the old card
                typingPrint("Answer in:")
                time.sleep(1)
                print()
                print("3...")
                time.sleep(1)
                print("2...")
                time.sleep(1)
                print("1...")
                time.sleep(1)
                typingPrint(f"The next card was {next_card}")
                print()
                player_points -= int(75)
                typingPrint(f"That is incorrect. You now have {player_points} points.")
                print()

        elif low_or_high == "l":
            low_or_high = card_number
            typingPrint("You guessed 'lower'")
            print()

            if low_or_high > next_card:
                # if the player guesses lower and the next card is lower than the old card
                typingPrint("Answer in:")
                time.sleep(1)
                print()
                print("3...")
                time.sleep(1)
                print("2...")
                time.sleep(1)
                print("1...")
                time.sleep(1)
                typingPrint(f"The next card was {next_card}")
                print()
                player_points += int(100)
                typingPrint(f"That is correct! You now have {player_points} points.")
                print()
            elif low_or_high < next_card:
                #if the player guesses lower and the next card is higher than the old card
                typingPrint("Answer in:")
                time.sleep(1)
                print()
                print("3...")
                time.sleep(1)
                print("2...")
                time.sleep(1)
                print("1...")
                time.sleep(1)
                typingPrint(f"The next card was {next_card}")
                print()
                player_points -= int(75)
                typingPrint(f"That is incorrect. You now have {player_points} points.")
                print()

        continue_playing = input("Would you like to play? Type 'y' for yes and 'n' for no: ")
        print()

    typingPrint(f"You have completed the game with {player_points} points.")
    print()
    typingPrint("Thank you for playing!")
    print()
    print()

card_guesses(player_points)