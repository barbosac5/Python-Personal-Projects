# Import random to make random selections
import random

# Choices 
choices = ["Rock", "Paper", "Scissors"]

# User input
guess = input("Rock, Paper, Scissors.... SHOOT! ")
if guess != "Rock" "Paper" or "Scissors":
    print("Not a choice")
    quit()      


# Computer make a random choice
CPU_choice = random.choice(choices)
print("You guessed " + guess + " while the CPU guessed.. " + CPU_choice)

# Determine win, loss or tie
if guess == "Rock" and CPU_choice == "Rock":
    print("It's a tie!")
elif guess == "Rock" and CPU_choice == "Paper":
    print("You Lose")
elif guess == "Rock" and CPU_choice == "Scissors":
    print("You Win!")

