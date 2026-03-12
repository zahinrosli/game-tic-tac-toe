# A classic Tic-Tac-Toe game
# Players 'X' and 'O' take turn inputing their position on the command line using numbers 1-9
# 1 | 2 | 3
# ---------
# 4 | 5 | 6
# ---------
# 7 | 8 | 9
#

# The Game Board 
board = {
    1: ' ', 2: ' ', 3: ' ',
    4: ' ', 5: ' ', 6: ' ',
    7: ' ', 8: ' ', 9: ' '
}

# Update the gameboard with the user input
def markBoard(position, mark):
    position = int(position)
    board[position] = mark
    return

# Print the game board as described at the top of this code skeleton
def printBoard():
    print(board[1],"|", board[2] ,"|", board[3])
    print("---------")
    print(board[4] ,"|", board[5] ,"|", board[6])
    print("---------")
    print(board[7] ,"|", board[8] ,"|", board[9])
    return

# Check for wrong input, this function should return True or False.
# True denoting that the user input is correct
# Need to check for wrong input (user is entering invalid position) or position is out of bound
# Another case is that the position is already occupied
def validateMove(position):
    position = int(position)
    if 1 <= position <= 9 and board[position] == ' ':
        return True
    return False

# List out all the winning combinations
winCombinations = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [1, 4, 7],
    [2, 5, 8],
    [3, 6, 9],
    [1, 5, 9],
    [3, 5, 7]
]

# Implement a logic to check if the previous winner just win
# This method should return with True or False
def checkWin(player):
    for combo in winCombinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] == player:
            return True
    return False

# Implement a function to check if the game board is already full
# For tic-tac-toe, tie bascially means the whole board is already occupied
# This function should return with boolean
def checkFull():
    for mark in board.keys():
        if board[mark] == ' ':
            return False
    return True

#########################################################

gameEnded = False
currentTurnPlayer = 'X'

# Entry point of the whole program
print('Game started: \n\n' +
    ' 1 | 2 | 3 \n' +
    ' --------- \n' +
    ' 4 | 5 | 6 \n' +
    ' --------- \n' +
    ' 7 | 8 | 9 \n')

# Game play logic:
# 1. Ask for user input and validate the input
# 2. Update the board
# 3. Check win or tie situation
# 4. Switch User
def switchUser():
    global currentTurnPlayer
    currentTurnPlayer = 'O' if currentTurnPlayer == 'X' else 'X'

def mainGame():
    global currentTurnPlayer, gameEnded
    gameEnded = False

    while not gameEnded:
        move = input(currentTurnPlayer + "'s turn, input: ")

        try:
            # We test the conversion here to catch the ValueError immediately
            int(move)
        except ValueError:
            print("Only put integer in this space!")
            continue
        
        if validateMove(move):
            markBoard(move, currentTurnPlayer)
            printBoard()
            
            if checkWin(currentTurnPlayer):
                print(f"Congratulations, {currentTurnPlayer} is the winner!")
                gameEnded = True
                break
            
            if checkFull():
                print("The game has ended in a tie.")
                gameEnded = True
                break
            
            switchUser()
        else:
            print("Wrong input! Please try again.") 

# Implement the feature for the user to restart the game after a tie or game over
def replay():
    global currentTurnPlayer
    
    while True:
        restart = input("Do you want to play again? (Y/N): ")

        if restart.lower() == "y":
            # Clear the board
            for mark in board.keys():
                board[mark] = ' '
            currentTurnPlayer = 'X' # Reset to player X
            mainGame() # Start the game again
        elif restart.lower() == "n":
            print("Thank you for playing!")
            break
        else:
            print("Wrong input! Please choose between 'Y' or 'N'only.")

# Trigger the game loop
mainGame()
replay()
