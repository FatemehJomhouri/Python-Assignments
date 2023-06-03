game_board=[["-","-","-"],["-","-","-"],["-","-","-"]]
while True:
    while True:
        print("Player 1")
        while True:
            row = int(input("please enter the row: "))
            if 1<=row<=3:
                break
            else:
                print("Please enter a number bet. 1 to 3")
        while True:
            col = int(input("Please enter the column: "))
            if 1<=col<=3:
                break
            else:
                print("Please enter a number bet. 1 to 3")
        if game_board[row-1][col-1]=="-":
            game_board[row-1][col-1]="x"
            break
        else:
            print("Select another Cell")
    for row in game_board:
        for cell in row:
            print(cell, end="")
        print()
    for i in range(3):
        if (game_board[i][0]==game_board[i][1]==game_board[i][2])and game_board[i][0]!="-":
            print("Player {} won!".format(game_board[i][0]))
            game_board=[["-","-","-"],
                        ["-","-","-"],
                        ["-","-","-"]]
    for j in range(3):
        if game_board[0][j]==game_board[1][j]==game_board[2][j] and game_board[0][j]!="-":
            print("Player {} won!".format(game_board[0][j]))
            game_board=[["-","-","-"],
                        ["-","-","-"],
                        ["-","-","-"]]
    if game_board[0][0]==game_board[1][1]==game_board[2][2] and game_board[0][0]!="-":
            print("Player {} won!".format(game_board[0][0]))
            game_board=[["-","-","-"],
                        ["-","-","-"],
                        ["-","-","-"]]
    if game_board[0][2]==game_board[1][1]==game_board[2][0] and game_board[0][2]!="-":
        print("Player {} won!".format(game_board[0][2]))
        game_board=[["-","-","-"],
                    ["-","-","-"],
                    ["-","-","-"]]
    while True:
        print("Player 2")
        while True:
            row = int(input("Please enter the row : "))
            if 1<=row<=3:
                break
            else:
                print("Please enter a number bet. 1 to 3: ")
        while True:
            col = int(input("Please enter the column: "))
            if 1<=col<=3:
                break
            else:
                print("Please enter a number bet. 1 to 3: ")
        if game_board[row-1][col-1]=="-":
            game_board[row-1][col-1]="o"
            break
        else:
            print("Select another Cell")
    for row in game_board:
        for cell in row:
            print(cell, end="")
        print()
    for i in range(3):
        if (game_board[i][0]==game_board[i][1]==game_board[i][2])and game_board[i][0]!="-":
            print("Player {} won!".format(game_board[i][0]))
            game_board=[["-","-","-"],
                        ["-","-","-"],
                        ["-","-","-"]]
    for j in range(3):
        if game_board[0][j]==game_board[1][j]==game_board[2][j] and game_board[0][j]!="-":
            print("Player {} won!".format(game_board[0][j]))
            game_board=[["-","-","-"],
                        ["-","-","-"],
                        ["-","-","-"]]
    if game_board[0][0]==game_board[1][1]==game_board[2][2] and game_board[0][0]!="-":
            print("Player {} won!".format(game_board[0][0]))
            game_board=[["-","-","-"],
                        ["-","-","-"],
                        ["-","-","-"]]
    if game_board[0][2]==game_board[1][1]==game_board[2][0] and game_board[0][2]!="-":
        print("Player {} won!".format(game_board[0][2]))
        game_board=[["-","-","-"],
                    ["-","-","-"],
                    ["-","-","-"]]
