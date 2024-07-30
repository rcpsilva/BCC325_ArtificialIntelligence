
def complete_sudoku(board):

    for row in board:
        for e in row:
            if e == 0:
                return False
            
    return True

def next_sudoku(board):
    
    for i in range(board.shape[0]):
        for j in range(board.shape[1]):
            if board[i][j] == 0:
                return i,j

    return None,None

def is_possible_sudoku(row,col,v,board):

    if v in board[row]:
        return False

    for i in range(board.shape[0]):
        if v == board[i][col]:
            return False    

    cell_row = (row//3) * 3
    cell_col = (col//3) * 3

    for i in range(cell_row, cell_row+3):
        for j in range(cell_col,cell_col+3):
            if board[i][j] == v:
                return False

    return True

def bk_sudoku(board):

    if complete_sudoku(board):
        print(board)
        input()
        return
    else:
        i,j = next_sudoku(board)
        for v in range(1,10):
            if is_possible_sudoku(i,j,v,board):
                board[i][j] = v
                bk_sudoku(board)
                board[i][j] = 0
        return


def is_possible(v,s):

    lin = len(s)
    col = v
    
    if col in s:
        return False
    
    for i in range(len(s)):
        if (abs(col-s[i]) == abs(lin-i)):
            return False
        
    return True

def bk_nqueen(n,s=[]):
    
    if len(s) == n:
        print(s)
        input()
        return
    else:
        for col in range(n):
            if is_possible(col,s):
                s.append(col)
                bk_nqueen(n,s)
                s.pop(-1)
        return
    
if __name__ == '__main__':

    #bk_nqueen(int(input("Digite o número de rainhas:")))
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

    bk_sudoku(hard_board)






