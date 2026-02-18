import numpy as np
tic_tac_toe = np.array([[1, -1, 0],
                         [0, -1, 1],
                         [-1, 0, 1]])
#Printing the Middle row of the board:
print("Middle row: ", tic_tac_toe[1])
#Printing the Last column of the board:
print("Last column: ", tic_tac_toe[:, 2])
#Now, to check who's winning:
def check_winner(tic_tac_toe):
  #To check who's winning, we'll take the sum of each column, row and diagonal. If any add up to 3, then X wins. If any add up to -3, then O wins.
    for i in range(3):
    #Check rows and columns
        row_sum = tic_tac_toe[i].sum()
        column_sum = tic_tac_toe[:, i].sum()

        if row_sum == 3 or column_sum == 3:
            return "X wins!"
        if row_sum == -3 or column_sum == -3:
            return "O wins!"
    #Check diagonals
    main_diag = tic_tac_toe.diagonal().sum()
    anti_diag = np.fliplr(tic_tac_toe).diagonal().sum()

    if main_diag == 3 or anti_diag == 3:
        return "X wins!"
    if main_diag == -3 or anti_diag == -3:
        return "O wins!"

    return "No winner yet."
print(check_winner(tic_tac_toe))
