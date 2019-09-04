from random import randint
from builtins import input
#initalise the board
board = []
#fill out 0 for the board
for x in range(5):
    board.append(["O"] * 5)
#make it pretty with spaces
def print_board(board):
    for row in board:
        print (" ".join(row))
#start and display board to player
print ("Let's play Battleship!")
print_board(board)
#define two random numbers
def random_row(board):
    return randint(0, len(board) - 1)

def random_col(board):
    return randint(0, len(board[0]) - 1)
#put the ship somewhere
ship_row = random_row(board)
ship_col = random_col(board)

#below will print the ship row and collum
#print ship_row
#print ship_col

# Everything from here on should go in your for loop!
# Be sure to indent four spaces!

#reset turn counter
turn=0
#start loop and run for 4 turns
for turn in range(0,4):
    guess_row = int(input("Guess Row:"))
    guess_col = int(input("Guess Col:"))
#win condition. break if successful
    if guess_row == ship_row and guess_col == ship_col:
        print ("Congratulations! You sunk my battleship!")
        break
    else:
#out of bounds check
        if (guess_row < 0 or guess_row > 4) or (guess_col < 0 or guess_col > 4):
          print ("Oops, that's not even in the ocean.")
#check "board" for previous guess
        elif(board[guess_row][guess_col] == "X"):
            print ("You guessed that one already.")
        else:
#if not a hit of out of bounds mark X at index
            print ("You missed my battleship!")
            board[guess_row][guess_col] = "X"
        print_board(board)
        print ("Turn", turn + 1)
#exit message when turn counter reached
        if turn == 3:
            print ("Game Over")
