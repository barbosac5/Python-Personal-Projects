# Import random module
from random import randint

board = []

# Creating game board
for x in range(5):
  board.append(["O"] * 5)

# Cleanliness
def print_board(board):
  for row in board:
    print(" "+ format(row))
print_board(board)

# Have program pick random row and col to guess
def random_row(board):
  return randint(0, len(board) - 1)

def random_col(board):
  return randint(0, len(board[0]) - 1)
ship_row = random_row(board)
ship_col = random_col(board)

# Used for testing
##print(ship_row)
##print(ship_col)

# Loop to have 4 guesses to sink the battleship or else game over
for turn in range(4):
  guess_row = int(input("Guess Row: "))
  guess_col = int(input("Guess Col: "))

# If you hit/miss battleship, hit the same spot, or completely miss the ocean
  if guess_row == ship_row and guess_col == ship_col:
    print("Congratulations! You sunk my battleship!")
    break
  else:
    if (guess_row < 0 or guess_row > 4) or (guess_col < 0 or guess_col > 4):
      print("Oops, that's not even in the ocean.")
    elif(board[guess_row][guess_col] == "X"):
      print("You guessed that one already.")
    else:
      print("You missed my battleship!")
      board[guess_row][guess_col] = "X"
      # Turn counter increses per turn
      print("Turn", turn + 1)
    if turn == 3:
      print("Game Over")

# Print updated board
  print_board(board)






