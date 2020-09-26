"""
Tic Tac Toe Player
"""

import math

X = "X"
O = "O"
EMPTY = None
ROUND = X

def isInit():
    return all(e is None for v in board for e in v)

# Returns starting state of the board.
def initial_state():
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]

# Returns player who has the next turn on a board. 
def player(board):
    if isInit:
        return X
    else:
        if ROUND == X:
            ROUND = O
            return O
        else:
            ROUND = X
            return X
            
# Returns set of all possible actions (i, j) available on the board.
def actions(board):
    possibles = []
    for i in range (0, 3):
        for j in range(0, 3):
            if board[i][j] == None:
                possibles.append((i,j))
    return possibles


# Returns the board that results from making move (i, j) on the board.
def result(board, action):
    raise NotImplementedError


# Returns the winner of the game, if there is one.
def winner(board):
    raise NotImplementedError


# Returns True if game is over, False otherwise.
def terminal(board):
    return False if utility(board) == 0 else True


# Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
def utility(board):
    turn = [X, O]
    for t in turn:
        diag2 = []
        aux = 2 # aux for secondary diagonal
        for i in range (0, 3):
            if all(e == t for e in board[i]):
                return 1 if t == X else -1
            col = []
            diag = []
            for j in range (0, 3):
                col.append(board[j][i])
                if i == j:
                    diag.append(board[i][j])
            if all(e == t for e in col): # check elements per column
                return 1 if t == X else -1
            diag2.append(board[i][aux])
            aux = aux - 1
        if all(e == t for e in diag): # check main diagonal
                return 1 if t == X else -1
        if all(e == t for e in diag2): # check secondary diagonal5
            return 1 if t == X else -1
    return 0
    raise NotImplementedError

# Returns the optimal action for the current player on the board.
def minimax(board):
    raise NotImplementedError
