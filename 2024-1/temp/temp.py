import os


def feasible(board,i,j,v):
    
    if v in board[i]:
        return False
    
    if v in board[:,j]:
        return False

    i_cell_start = i//3*3
    j_cell_start = j//3*3

    for i in range(i_cell_start,i_cell_start+3):
        for j in range(j_cell_start,j_cell_start+3):
            if board[i][j] == v:
                return False

    return True

def next(board):
    for i in range(9):
        for j in range(9):
            if board[i][j]==0:
                return i,j

    return -1,-1

def is_complete(board):

    i,j = next(board)

    if (i==-1) and (j==-1):
        return True
    else:
        return False
  

def search(board):
  
    if is_complete(board):
        print(board)
        return
    else:
        i,j = next(board)
        for v in range(1,10):
            if feasible(board,i,j,v):
                board[i][j] = v
                search(board)
                board[i][j] = 0
        return 

if __name__ == '__main__':
    import numpy as np

    empty_board = np.zeros((9,9))
    
    hard_board = np.array([
    [8, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 3, 6, 0, 0, 0, 0, 0],
    [0, 7, 0, 0, 9, 0, 2, 0, 0],
    [0, 5, 0, 0, 0, 7, 0, 0, 0],
    [0, 0, 0, 0, 4, 5, 7, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 3, 0],
    [0, 0, 1, 0, 0, 0, 0, 6, 8],
    [0, 0, 8, 5, 0, 0, 0, 1, 0],
    [0, 9, 0, 0, 0, 0, 4, 0, 0]
    ])

    easy_board = np.array([
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
    ])

    search(hard_board)