import os
import time

def print_game(game):
    os.system('cls')
    print()
    for row in game:
        print(row)
    time.sleep(0.1)
        
def violate_constraints(game,i,j,v):

    for cell in game[i]:
        if v == cell:
            return True
        
    for row in game:
        if row[j] == v:
            return True
        
    igroup = (i//3)*3
    jgroup = (j//3)*3

    for i in range(3):
        for j in range(3):
            if game[igroup+i][jgroup+j] == v:
                return True
    
    return False


def is_solution(game):
    for row in game:
        for cell in row:
            if cell == 0:
                return False
    return True

def backtrack_sudoku(game):
    if is_solution(game):
        print_game(game)
    else:
        #find free position
        for i in range(9):
            for j in range(9):
                if game[i][j] == 0:
                    for v in range(1,10):
                        if not violate_constraints(game, i, j, v):
                            game[i][j] = v
                            #print_game(game)
                            backtrack_sudoku(game)
                            game[i][j] = 0
                    return

if __name__ == '__main__':
    easy_game = [[0,0,0,7,5,0,4,9,0],
             [0,4,5,6,9,0,0,1,8],
             [0,0,6,0,0,0,7,0,0],
             [9,8,0,2,0,0,0,0,0],
             [2,0,7,1,0,8,0,0,0],
             [0,0,3,0,0,5,8,0,7],
             [4,2,0,0,6,7,1,8,0],
             [5,0,0,0,2,0,0,7,4],
             [3,0,0,5,1,0,9,0,2]]

    evil_game = [[1,0,0,0,0,9,0,0,0],
             [0,0,0,0,2,0,4,0,0],
             [0,5,9,8,0,0,0,0,3],
             [6,0,0,7,0,0,0,0,0],
             [0,1,7,0,0,4,3,0,0],
             [8,0,0,0,0,0,0,0,1],
             [0,0,0,0,0,8,0,9,0],
             [0,7,3,9,0,0,0,0,5],
             [0,0,6,0,0,0,0,0,0]]

    backtrack_sudoku(easy_game)