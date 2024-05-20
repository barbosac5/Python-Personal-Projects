# Import random to make random selections
import random

# Choices 
choices = ["Rock", "Paper", "Scissors"]
 

# Game count
game_count  = 0

# Loop to count best of 3 games
while game_count < 3:     
    ## User input
    guess = input("Rock, Paper, Scissors.... SHOOT! ")
    #guess = guess.lower()

    ## If user makes invalid guess
    if guess != "Rock" "Paper" or "Scissors":
        print("Not a choice")
        quit()

    ## Computer make a random choice
    CPU_choice = random.choice(choices)
    print("You guessed " + guess + " while the CPU guessed.. " + CPU_choice)
    game_count += 1

    ## Determine win, loss or tie
    if guess == "Rock" and CPU_choice == "Rock":
        print("It's a tie!")
    elif guess == "Rock" and CPU_choice == "Paper":
        print("You Lose")
    elif guess == "Rock" and CPU_choice == "Scissors":
        print("You Win!")
    

    
    

