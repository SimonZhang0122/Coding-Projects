"""
Part 2 of the Tic Tac Toe project, dealing with user input by asking for a colume and row position of where they want to place their move.
"""
map = [[0,0,0],
       [0,0,0],
       [0,0,0]]

def player():
    turn = 1
    while turn < 10:
        if turn % 2 == 1:
            print(map[0])
            print(map[1])
            print(map[2])
            strcol, strrow = input("Player 1 make your move: ").split()
            col = int(strcol) - 1
            row = int(strrow) - 1
            map[col][row] = 'X'
            turn = turn + 1
        else:
            print(map[0])
            print(map[1])
            print(map[2])            
            strcol, strrow = input("Player 2 make your move: ").split()
            col = int(strcol) - 1
            row = int(strrow) - 1
            map[col][row] = 'O'
            turn = turn + 1

player()
print(map)