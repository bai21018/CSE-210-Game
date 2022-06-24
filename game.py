#this is the hilo game
import random as r

player_points = int(300)

def card_guesses(player_points):
    continue_playing = "y"
    
    while continue_playing == "y":
        card_number = r.randint(1,13)
        next_card = r.randint(1,13)
    
        print(f"The current card is {card_number}")
        low_or_high = input("Is the next card higher or lower? ")
        print(f"The next card was {next_card}")

        #if the player guesses higher
        if low_or_high == "h":
            low_or_high = card_number
            print("You guessed 'higher'")
            print(f"low or high {low_or_high}")
            print(f"next card {next_card}")
            print(f"card number {card_number}")
            print()

            if low_or_high >= next_card:
                # if the player guesses higher and the next card is higher than the old card 
                player_points += int(100)
                print("low or high is greater than next card!")
                print(f"That is correct! You now have {player_points} points.")
                print()
            elif low_or_high < next_card:
                #if the player guesses higher and the next card is lesser than the old card
                player_points -= int(75)
                print(f"That is incorrect. You now have {player_points} points.")
                print("low or high is less than next card!")
                print()

        elif low_or_high == "l":
            low_or_high = card_number
            print("You guessed 'lower'")
            print(f"low or high {low_or_high}")
            print(f"next card {next_card}")
            print(f"card number {card_number}")
            print()

            if low_or_high < next_card:
                # if the player guesses lower and the next card is lower than the old card 
                player_points += int(100)
                print("low or high is greater than next card!")
                print(f"That is correct! You now have {player_points} points.")
                print()
            elif low_or_high > next_card:
                #if the player guesses lower and the next card is higher than the old card
                player_points -= int(75)
                print(f"That is incorrect. You now have {player_points} points.")
                print("low or high is less than next card!")
                print()

        continue_playing = input("Would you like to play? Type 'y' for yes and 'n' for no: ")
        print()

    print(f"You have completed the game with {player_points} points.")
    print("Thank you for playing!")    

card_guesses(player_points)