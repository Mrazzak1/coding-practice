
board = [['_', '_', '_'],['_', '_', '_'],['_', '_', '_']]

def PrintBoard():
    for i in range(0, len(board)):  
        for j in range(0, len(board[0])):
            print(board[i][j], end =" ")
        print('')
    print('')


def HasWon():

    #horizointal
    for j in range(0, 3):
        won = True
        symbol = board[j][0]
        for i in range(0, 3):
            if board[j][i] != symbol or board[j][0] == "_":
                won = False
        if won == True:
            return True

    #vertical
    for j in range(0, 3):
        won = True
        symbol = board[0][j]
        for i in range(0, 3):
            if board[i][j] != symbol or board[0][j] == "_":
                won = False
        if won == True:
            return True

    #diagonal
    row = 0
    val = board[0][0]
    won = True
    for col in range(0, 3):
        if board[row][col] != val or board[row][col] == '_':
            won = False
        row = row + 1
        if won == True:
            return True

    #diagonal
    row = 2
    val = board[2][0]
    won = True
    for col in range(0, 3):
        if board[row][col] != val or board[row][col] == '_':
            won = False
        row = row - 1
        if won == True:
            return True        
            
    return False
    
    


symbol1 = input("Please choose the symbol for player one. (Any letter): ")
print("Your symbol is " + symbol1)
symbol2 = input("Please choose the symbol for player two. (Any letter): ")
PrintBoard()

player = 1

while True:

    row = int(input("Enter the row position player " + str(player) + ": "))
    column = int(input("Enter the column position of " + str(player) + ": "))

    if row < 0 or row > len(board)-1 or column < 0 or column > len(board[1])-1 or board[row][(column)] != '_':
        print("Invalid position.")
        continue

    if player == 1:
        board[row][column] = symbol1
    elif player == 2:
        board[row][column] = symbol2
    
    PrintBoard()
    
    if HasWon() == True:
        print("Game Finished")
        break

    if player == 1:
        player = 2
    elif player == 2:
        player = 1
        









