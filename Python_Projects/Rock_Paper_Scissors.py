# Import random to make random selections
import random

# Choices 
choices = ["Rock", "Paper", "Scissors"]
 
# Set intial game count
game_count = 0

## User input
prompt = print("Rock, Paper, Scissors, SHOOT:")
guess = input("")
    #guess = guess.lower()

# Loop to count best of 3 games
while game_count < 2:     
        
    ## Computer make a random choice
    CPU_choice = random.choice(choices)
    print("You guessed " + guess + " while the CPU guessed.. " + CPU_choice)
    game_count += 1
    
    ## Determine win, loss or tie (for Rock)
    if guess == "Rock" and CPU_choice == "Rock":
        print("It's a tie!")
        print(input("Lets go Again: "))
    elif guess == "Rock" and CPU_choice == "Paper":
        print("You Lose")
        print(input("Lets go Again: "))
    elif guess == "Rock" and CPU_choice == "Scissors":
        print("You Win!")
        print(input("Lets go Again: "))
    
    ## Determine win, loss or tie (for Paper)
    elif guess == "Paper" and CPU_choice == "Rock":
        print("You Win!")
        print(input("Lets go Again: "))
    elif guess == "Paper" and CPU_choice == "Paper":
        print("It's a tie")
        print(input("Lets go Again: "))
    elif guess == "Paper" and CPU_choice == "Scissors":
        print("You Lose!")
        print(input("Lets go Again: "))

    ## Determine win, loss or tie (for Scissors)
    elif guess == "Scissors" and CPU_choice == "Rock":
        print("You Lose!")
        print(input("Lets go Again: "))
    elif guess == "Scissors" and CPU_choice == "Paper":
        print("You Win")
        print(input("Lets go Again: "))
    elif guess == "Scissors" and CPU_choice == "Scissors":
        print("It's a tie")
        print(input("Lets go Again: "))
    else:
        print("Not a valid choice")
        quit()

if game_count == 3:
    print("Game Over")



    
    

    
    

