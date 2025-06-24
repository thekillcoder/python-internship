import random
Board =[ "_", "_", "_", 
        "_", "_", "_",
        "_", "_", "_",]

CurrentPlayer = "x"
winner = None
gameRunner = True

#Printing the game board
def printBoard(Board):
    print(Board[0] + " | " + Board[1] + " | " + Board[2])
    print("_________")
    print(Board[3] + " | " + Board[4] + " | " + Board[5])
    print("_________")
    print(Board[6] + " | " + Board[7] + " | " + Board[8])
printBoard(Board)

#Taking player Input
def playerInput(Board):
    inp = int(input("Enter a Number from 1-9: "))
    if inp >= 1 and inp <= 9 and Board[inp-1] == "_":
        Board[inp-1] = CurrentPlayer
    else:
        print("Ooops player is already in that spot")

#check for the win or tie
def checkHorizontle(Board):
    global winner
    if Board[0] == Board[1] == Board[2] and Board[0] != "_":
        winner = Board[0]
        return True
    elif Board[3] == Board[4] == Board[5] and Board[3] != "_":
        winner = Board[3]
        return True
    elif Board[6] == Board[7] == Board[8] and Board[6] != "_":
        winner = Board[6]
        return True
    
def checkVertical(Board):
    global winner
    if Board[0] == Board[3] == Board[6] and Board[0] != "_":
        winner = Board[0]
        return True
    elif Board[1] == Board[4] == Board[7] and Board[1] != "_":
        winner = Board[1]
        return True
    elif Board[2] == Board[5] == Board[8] and Board[2] != "_":
        winner = Board[2]
        return True
    
def checkDiag(Board):
    global winner
    if Board[0] == Board[4] == Board[8] and Board[0] != "_":
        winner = Board[0]
        return True
    elif Board[2] == Board[4] == Board[6] and Board[2] != "_":
        winner = Board[2]
        return True
    
def checkTie(Board):
    global gameRunner
    if "_" not in Board:
      printBoard(Board)
      print(" It is a Tie! ")
      gameRunner = False

def checkWin(Board):
    if checkDiag(Board)  or checkHorizontle(Board)  or checkVertical(Board):
     print(f"The winner is {winner}")


#switch the player

def switchPlayer():
    global CurrentPlayer
    if CurrentPlayer == "x":
        CurrentPlayer = "0"
    else:
        CurrentPlayer = "x"
#Computer
def computer(Board):
    while CurrentPlayer == "0":
        position = random.randint(0, 8)
        if Board[position] == "_":
            Board[position] = "0"
            switchPlayer()

#check again win or tie

while gameRunner:
    printBoard(Board)
    playerInput(Board)
    checkWin(Board)
    checkTie(Board)
    switchPlayer()
    computer(Board)
    checkWin(Board)
    checkTie(Board)




