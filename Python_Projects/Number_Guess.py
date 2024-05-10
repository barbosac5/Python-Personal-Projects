# imports
import math
import random

# Function for number guess
def number_guess(n):
    # Have starting guess count set to 0
    guess_count = 0
    print("Welcome to the Number Guessing Game. You will have 3 tries to guess my number. Good luck!")
    while guess_count < 3:
        # Have program generate a random number for the player to guess
        n  = random.randint(1, 10)
        # Prompt to allow user to input their first, second, third, etc. guess
        guess = int(input("What is your guess?: "))
        if guess == n:
            print("You got it! Good job! To took you " + str(guess_count) + " attempts!")
            break
        else:
            if guess_count == 2:
                print("Game Over")
                break
            elif guess > n:
                print("Too high. Try again.")
                guess_count += 1
            elif guess < n:
                print("Too low. Try again")
                guess_count += 1
        
       
# Call the function
number_guess(9)