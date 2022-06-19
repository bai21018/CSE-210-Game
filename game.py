#this is the hilo game
import random as r

player_points = int(600)

random_number = r.randint(1, 13)

continue_playing = input("Would you like to play? Type 'y' for yes and 'n' for no: ")
player_guess = input("Enter a number: ")



while continue_playing != "n":
    if int(player_guess) > random_number:
        print(f"You guessed '{player_guess}' incorrectly and have lost 75 points")
        player_points += int(-75)
    else:
        print(f"You guessed '{player_guess}' and have been awarded 100 points!")
        player_points = player_points + int(100)

        
print(random_number)
print(player_points)


    
