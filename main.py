"""
    @author: Eng Ossama Samir
"""

"""
    Let O for AI agent
    Description :
        first for each board alone the function loop for columns ,
        rows and diagonals and set for each cell wight
        What does wight mean?
            when we loop in column , row or diagonal if we found O then increase 
            wight by 1 and if we found X increase wight by 1
            after set wight for each cell then we loop for each cell again and 
            git max wight .
            the cell have max wight it has priority to put O in it            
"""
board =[[["X","0","0","0"],
          ["0","0","0","0"],
          ["0","0","0","0"],
          ["0","0","0","0"]],
                             [["0","0","0","0"],
                              ["0","X","0","0"],
                              ["0","0","0","0"],
                              ["0","0","0","0"]],
                                                 [["0","0","0","0"],
                                                  ["0","0","0","0"],
                                                  ["0","0","X","0"],
                                                  ["0","0","0","0"]],
                                                                     [["0","0","0","0"],
                                                                      ["0","0","0","0"],
                                                                      ["0","0","0","0"],
                                                                      ["0","0","0","X"]]]

b = [[["-",0],["-",0],["-",0],["-",0]],
     [["-",0],["-",0],["-",0],["-",0]],
     [["-",0],["-",0],["-",0],["-",0]],
     [["-",0],["-",0],["-",0],["-",0]]]
def heuristicFunction(board):
    for i in range(4):
        for j in range(4):
            setWigh(board,i,j)
    maxWight, maxWightRow, maxWightColumn = getMax(board)
    board[maxWightRow][maxWightColumn][0]="O"
    reSetWigh(board,maxWightColumn,maxWightRow)

def setWigh(board,column,row):
    """
        this function take two parameter x and y .
        and check for  column, row and diagonal for this cell :
            if found X increase cell wight by 1
            if found O decrease cell wight by 1
    """
    # check if the cell has X or O then don't calculate wight
    if board[row][column][0] == "O" or board[row][column][0] == "X":
        board[row][column][1] = 0
    else :
        # check for row
        for i in range(4):
            if board[row][i][0] == "O":
                board[row][column][1] -= 0
            if board[row][i][0] == "X":
                board[row][column][1] += 1
        # check for column
        for i in range(4):
            if board[i][column][0] == "O":
                board[row][column][1] += 0
            if board[i][column][0] == "X":
                board[row][column][1] += 1
        # check diagonal
        if row == column :
            for i in range(4):
                if board[i][i][0] == "O":
                    board[row][column][1] -= 0
                if board[i][i][0] == "X":
                    board[row][column][1] += 1
        if (column == 3 and row == 0) | (column == 2 and row == 1) | (column == 1 and row == 2) | (column == 0 and row == 3) :
            for i in range(4):
                if board[i][4-1-i][0] == "O":
                    board[row][column][1] -= 0
                if board[i][4-1-i][0] == "X":
                    board[row][column][1] += 1

def reSetWigh(board,column,row):
    # check if the cell has X or O then don't calculate wight
    if board[row][column][0] == "O" or board[row][column][0] == "X":
        board[row][column][1] = 0
    else :
        # check for row
        for i in range(4):
            if board[row][i][0] == "O":
                board[row][column][1] = 0
            if board[row][i][0] == "X":
                board[row][column][1] = 0
        # check for column
        for i in range(4):
            if board[i][column][0] == "O":
                board[row][column][1] = 0
            if board[i][column][0] == "X":
                board[row][column][1] = 0
        # check diagonal
        if row == column :
            for i in range(4):
                if board[i][i][0] == "O":
                    board[row][column][1] = 0
                if board[i][i][0] == "X":
                    board[row][column][1] = 0
        if (column == 3 and row == 0) | (column == 2 and row == 1) | (column == 1 and row == 2) | (column == 0 and row == 3) :
            for i in range(4):
                if board[i][4-1-i][0] == "O":
                    board[row][column][1] = 0
                if board[i][4-1-i][0] == "X":
                    board[row][column][1] = 0
def getMax(board):
    """
        this function loop for all cell in board and get max wight
        return : max wight and his index
    """
    max_weight = float('-inf')
    max_weight_row = 0
    max_weight_col = 0

    for row_index, row in enumerate(board):
        for col_index, item in enumerate(row):
            value = item[1]
            if value > max_weight:
                max_weight = value
                max_weight_row = row_index
                max_weight_col = col_index
    return max_weight, max_weight_row, max_weight_col
def printBoard(board):
    for i in b:
        for j in i:
            print(f"{j[0]}\t",end="")
        print()
    print("----------------------")



printBoard(b)
for i in range(16) :
    inputRow = input("Enter Row ")
    try:
        inputRow = int(inputRow)
    except ValueError:
        print("Please enter a valid integer.")
    if inputRow == -1 :
        print("Game Ended")
        break
    inputColumn = input("Enter Column ")
    try:
        inputColumn = int(inputColumn)
    except ValueError:
        print("Please enter a valid integer.")
    b[inputRow][inputColumn][0] = "X"
    printBoard(b)
    heuristicFunction(b)
    print("*********************")
    printBoard(b)



# the following code for display board with weight
'''
move = ""
for lyear in board :
    for row in lyear :
        index = 0
        for item in row :
            if index == 0 :
                print(move,f"{item}\t", end="")
            else:
                print(f"{item}\t",end="")
            index += 1
        print()
    move += "            "
'''