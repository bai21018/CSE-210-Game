#this is the hilo game
import random as r

player_points = int(300)

def card_guesses(player_points):
    continue_playing = "y"
    
    while continue_playing == "y":
        # card_number = r.randint(1,13)
        # next_card = r.randint(1,13)
        card_number = int(2)
        next_card = int(2)
    
        print(f"The current card is {card_number}")

        low_or_high = input("Is the next card higher or lower? ")
        print(f"The next card was {next_card}")

        if low_or_high == "h":
            low_or_high = int(next_card) + int(1)
            print("line 20")
            print()
            print("You guessed 'higher'")
            print(low_or_high)

            print()

        elif low_or_high == "l":
            low_or_high = int(next_card) - int(1)
            print("line 27")
            print()
            print("You guessed 'lower'")
            print(low_or_high)
            print()

        if int(low_or_high) < next_card:
            player_points += int(100)
            print("line 34")
            print()
            print(f"card number: {card_number}, next card : {next_card}")
            print(f"That is correct, the next card is smaller than the old. You now have {player_points}")
            print()
            print(f"elif low or high >= next card, low or high = {low_or_high}, card number = {card_number}, next card = {next_card}, player points = {player_points}")

        elif int(low_or_high) > next_card:
            player_points += int(100)
            print("line 40")
            print()
            print(f"card number: {card_number}, next card : {next_card}")
            print(f"That is correct, the new card is larger than the old. you now have {player_points}")
            print() 
            print(f"elif low or high <= next card, low or high = {low_or_high}, card number = {card_number}, next card = {next_card}, player points = {player_points}")
        
        elif low_or_high == next_card:
            player_points += (100)
            print("line 52")
            print(f"The numbered card was the same. You get points for this! You now have {player_points} points.")
            print()
            print(f"same number, elif low or high == next card, low or high = {low_or_high}, card number = {card_number}, next card = {next_card}, player points = {player_points}")
        

        else:
            player_points -= int(75)
            print(f"That is incorrect. You now have {player_points}")

        continue_playing = input("Would you like to play? Type 'y' for yes and 'n' for no: ")
        print()

    print(card_number)
    print(next_card)
    print(player_points)    

card_guesses(player_points)