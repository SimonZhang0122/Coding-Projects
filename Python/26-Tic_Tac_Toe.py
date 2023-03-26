"""
Making a game of tic tac toe with 4 parts, project 24, 26, 27 and 29. 
Part 1 of the Tic Tac Toe project, 24-ask the user what size game board they want to draw, and draw it for them to the screen using Python’s print statement.
Part 2 of the Tic Tac Toe project, 26-check whether someone has won a game, not worrying how the moves are made.
Part 3 of the Tic Tac Toe project, 27-dealing with user input by asking for a colume and row position of where they want to place their move.
Part 4 of the Tic Tac Toe project, 29- put all these three components together to make a two-player Tic Tac Toe game. 
"""

import contextlib

ascore = 0
bscore = 0


def winType(type):
    
    if type == "diag":
        print("\n")
        if map[0][0] == map[1][1] == map[2][2] == "X":
            print_map(map)
            print("Player 1 wins diagonally!")
            scoreKeeper(1)
        elif map[0][0] == map[1][1] == map[2][2] == "O":
            print_map(map)
            print("Player 2 wins diagonally!")
            scoreKeeper(2)
        elif map[0][2] == map[1][1] == map[2][0] == "X":
            print_map(map)
            print("Player 1 wins diagonally!")
            scoreKeeper(1)
        else:
            print_map(map)
            print("Player 2 wins diagonally!")
            scoreKeeper(2)
            
    if type == "ver":
        print("\n")
        if map[0][0] == map[1][0] == map[2][0] == "X":
            print_map(map)
            print("Player 1 wins vertically!")
            scoreKeeper(1)
        elif map[0][0] == map[1][0] == map[2][0] == "O":
            print_map(map)
            print("Player 2 wins vertically!")
            scoreKeeper(2)
        elif map[0][1] == map[1][1] == map[2][1] == "X":
            print_map(map)
            print("Player 1 wins vertically!")
            scoreKeeper(1)
        elif map[0][1] == map[1][1] == map[2][1] == "O":
            print_map(map)
            print("Player 2 wins vertically!")
            scoreKeeper(2)
        elif map[0][2] == map[1][2] == map[2][2] == "X":
            print_map(map)
            print("Player 1 wins vertically!")
            scoreKeeper(1)
        else:
            print_map(map)
            print("Player 2 wins vertically!")
            scoreKeeper(2)
    
    if type == "hor":
        print("\n")
        if map[0][0] == map[0][1] == map[0][2] == "X":
            print_map(map)
            print("Playe 1 wins horizontally!")
            scoreKeeper(1)
        elif map[0][0] == map[0][1] == map[0][2] == "O":
            print_map(map)
            print("Playe 2 wins horizontally!")
            scoreKeeper(2)
        elif map[1][0] == map[1][1] == map[1][2] == "X":
            print_map(map)
            print("Playe 1 wins horizontally!")
            scoreKeeper(1)
        elif map[1][0] == map[1][1] == map[1][2] == "O":
            print_map(map)
            print("Playe 2 wins horizontally!")
            scoreKeeper(2)
        elif map[2][0] == map[2][1] == map[2][2] == "X":
            print_map(map)
            print("Playe 1 wins horizontally!")
            scoreKeeper(1)
        else:
            print_map(map)
            print("Playe 2 wins horizontally!")
            scoreKeeper(2)


def winChecker(map):
    global type
    if (
            (map[0][0] != " " and map[0][0] == map[1][1] == map[2][2]) or 
            (map[0][2] != " " and map[0][2] == map[1][1] == map[2][0])
        ):
        winType("diag")
    elif(
            (map[0][0] != " " and map[0][0] == map[1][0] == map[2][0]) or
            (map[0][1] != " " and map[0][1] == map[1][1] == map[2][1]) or
            (map[0][2] != " " and map[0][2] == map[1][2] == map[2][2])
        ):
        winType("ver")
    elif(
            (map[0][0] != " " and map[0][0] == map[0][1] == map[0][2]) or
            (map[1][0] != " " and map[1][0] == map[1][1] == map[1][2]) or
            (map[2][0] != " " and map[2][0] == map[2][1] == map[2][2])
        ):
        winType("hor")
    elif any(" " in ls for ls in map) == False:
        print("No one wins.")


def print_map(map):
    print(" === === ===", end = "\n| ")
    print(*map[0], sep = " | ", end = " |\n === === ===\n| ")
    print(*map[1], sep = " | ", end = " |\n === === ===\n| ")
    print(*map[2], sep = " | ", end = " |\n === === ===\n")

    
def player():
    global map
    map = [[" "," "," "],
           [" "," "," "],
           [" "," "," "]]
    turn = 1
    while turn < 10:
        if turn % 2 == 1:
            print_map(map)
            try:
                strcol, strrow = input("Player 1 make your move: ").split()
            except:
                print("Error! Please input 2 numbers seperated by space.")
                strcol, strrow = input("Player 1 make your move: ").split()
                col = int(strcol) - 1
                row = int(strrow) - 1                
            else:
                col = int(strcol) - 1
                row = int(strrow) - 1
            if col > 3 or row > 3:
                print("\nInvalid input! Placement out of bound.\n")
                continue
            if map[col][row] == " ":
                map[col][row] = "X"
            else:
                print("\nInvalid move! Space is already taken.\n")
                continue
            turn = turn + 1
            winChecker(map)
            print("\n")

        else:
            print_map(map)
            try:
                strcol, strrow = input("Player 2 make your move: ").split()
            except:
                print("Error! Please input 2 numbers seperated by space.")
                strcol, strrow = input("Player 2 make your move: ").split()
                col = int(strcol) - 1
                row = int(strrow) - 1                
            else:
                col = int(strcol) - 1
                row = int(strrow) - 1
            if col > 3 or row > 3:
                print("\nInvalid input! Placement out of bound.\n")
                continue            
            if map[col][row] == " ":
                map[col][row] = "O"
            else:
                print("\nInvalid move! Space is already taken.\n")
                continue
            turn = turn + 1
            winChecker(map)
            print("\n")


def scoreKeeper(who):
    global ascore
    global bscore
    if who == 1:
        ascore += 1
    if who == 2:
        bscore += 1
    print("The current score is Player1: " + str(ascore) + " to " + str(bscore) + " :Player2.")
    choice = input("Would you like to play again? (Y/N): ")
    while choice not in ["Y", "y", "N", "n"]:
        print("Invalid input, please type 'Y' or 'N'")
    else:
        if choice == "Y" or choice == "y":
            player()
        else:
            exit()


player()