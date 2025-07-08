import random

print("Welcome to Connect Four")
print("-----------------------")

possible_letters = ["A", "B", "C", "D", "E", "F", "G"]
rows = 6
cols = 7
gameBoard = [["" for _ in range(cols)] for _ in range(rows)]

def printGameBoard():
    print("\n   A    B    C    D    E    F    G", end="")
    print("\n   +----+----+----+----+----+----+----+")
    for y in range(rows):
        print(y, " |", end="")
        for x in range(cols):
            cell = gameBoard[y][x]
            if cell == "🔵" or cell == "🔴":
                print(" ", cell, end=" |")
            else:
                print("   ", end=" |")
        print("\n   +----+----+----+----+----+----+----+")

def modifyArray(coordinate, chip):
    y, x = coordinate
    gameBoard[y][x] = chip

def checkForWinning(chip):
    # Horizontal check
    for y in range(rows):
        for x in range(cols - 3):
            if all(gameBoard[y][x+i] == chip for i in range(4)):
                print(f"\nGame over! {chip} wins! Thank you for playing :)")
                return True
    # Vertical check
    for x in range(cols):
        for y in range(rows - 3):
            if all(gameBoard[y+i][x] == chip for i in range(4)):
                print(f"\nGame over! {chip} wins! Thank you for playing :)")
                return True
    # Diagonal (top-left to bottom-right)
    for y in range(rows - 3):
        for x in range(cols - 3):
            if all(gameBoard[y+i][x+i] == chip for i in range(4)):
                print(f"\nGame over! {chip} wins! Thank you for playing :)")
                return True
    # Diagonal (bottom-left to top-right)
    for y in range(3, rows):
        for x in range(cols - 3):
            if all(gameBoard[y-i][x+i] == chip for i in range(4)):
                print(f"\nGame over! {chip} wins! Thank you for playing :)")
                return True
    return False

def coordinateParser(letter):
    col = possible_letters.index(letter.upper())
    for row in reversed(range(rows)):
        if gameBoard[row][col] == "":
            return [row, col]
    return None  # Column is full

winner = False
turnCounter = 0

while not winner:
    printGameBoard()
    if turnCounter % 2 == 0:
        # Player Turn
        while True:
            user_input = input("\nChoose a column (A-G): ").strip().upper()
            if user_input not in possible_letters:
                print("Invalid input. Please choose A-G.")
                continue
            coordinate = coordinateParser(user_input)
            if coordinate:
                modifyArray(coordinate, '🔵')
                break
            else:
                print("That column is full. Try another.")
        winner = checkForWinning('🔵')
    else:
        # Computer Turn
        print("\nComputer is making a move...")
        while True:
            cpu_letter = random.choice(possible_letters)
            cpu_coordinate = coordinateParser(cpu_letter)
            if cpu_coordinate:
                modifyArray(cpu_coordinate, '🔴')
                break
        winner = checkForWinning('🔴')

    turnCounter += 1

    # Optional: Detect draw
    if turnCounter >= rows * cols and not winner:
        printGameBoard()
        print("\nIt's a draw! Thank you for playing :)")
        break
 