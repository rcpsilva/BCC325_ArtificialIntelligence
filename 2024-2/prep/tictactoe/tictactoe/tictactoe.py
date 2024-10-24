"""
Tic Tac Toe Player
"""

import math
from copy import deepcopy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]

def player(board):
    """
    Returns the player who has the next turn on the board.
    """
    countx = sum(row.count(X) for row in board)
    counto = sum(row.count(O) for row in board)

    # If X has fewer moves, it's X's turn, otherwise it's O's turn.
    if countx <= counto:
        return X
    else:
        return O

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    return {(i, j) for i in range(len(board)) for j in range(len(board[i])) if board[i][j] == EMPTY}

def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """

    if (action[0] not in [0,1,2]) or (action[1] not in [0,1,2]) or (board[action[0]][action[1]]!=EMPTY):
        raise ValueError(f'The action {action} in not valid')

    new_board = deepcopy(board)

    new_board[action[0]][action[1]] = player(new_board)
    return new_board

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    
    # Check rows
    for row in board:
        if row[0] == row[1] == row[2]:
            return row[0]

    # Check columns
    for j in range(len(board)):
        if board[0][j] == board[1][j] == board[2][j]: 
            return board[0][j]


    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2]:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0]:
        return board[0][2]


    return None

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """

    if winner(board):
        return True

    for row in board:
        for e in row:
            if e == EMPTY:
                return False

    return True 

def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == O:
        return -1
    elif winner(board) == X:
        return 1
    else:
        return 0

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    
    if player(board) == X:
        _ , a = max_action(board)
        return a
    else: 
        _ , a = min_action(board)
        return a

def max_action(board):

    if terminal(board):
        return utility(board), None
    
    v = -math.inf
    a = None

    for action in actions(board):
        v_ , _ = min_action(result(board,action))
        if v_ > v:
            v = v_
            a = action
    
    return v,a

def min_action(board):

    if terminal(board):
        return utility(board), None
    
    v = math.inf
    a = None

    for action in actions(board):
        v_ , _ = max_action(result(board,action))
        if v_ < v:
            v = v_
            a = action
    
    return v,a

if __name__ == '__main__':

    board = initial_state()
    board[0][0] = X
    
    act = actions(board)

    print(player(board))
    print(act)