"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None

def isInit(board):
    return all(e is None for v in board for e in v)

# Returns starting state of the board.
def initial_state():
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def count_empty(board):
    return len([e for listL in board for e in listL if e is EMPTY])
    

# Returns player who has the next turn on a board. 
def player(board):
    if isInit(board):
        return X
    else:
        lenght = count_empty(board)
        if lenght % 2 == 0: # if even, O turn
            return O
        else:
            return X


def get_letter(board):
    return O if count_empty(board) % 2 == 0 else X

def actions(board):
    possibles = []
    for i in range (0, 3):
        for j in range(0, 3):
            if board[i][j] == EMPTY:
                possibles.append((i,j))
    return possibles

# Returns the board that results from making move (i, j) on the board.
def result(board, action):
    aux = copy.deepcopy(board)
    i, j = action
    if i >= 0 and i <=2 and j >= 0 and j <= 2 and aux[i][j] is EMPTY:
        aux[i][j] = get_letter(board)
        return aux
    else:
        raise Exception("Index out of range")

# Returns the winner of the game, if there is one.
def winner(board):
    turn = [X, O]
    for t in turn:
        diag2 = []
        aux = 2 # aux for secondary diagonal
        for i in range (0, 3): # check elements per line
            if all(e == t for e in board[i]):
                return t
            col = []
            diag = []
            for j in range (0, 3):
                col.append(board[j][i])
            if all(e == t for e in col): # check elements per column
                return t
            diag2.append(board[i][aux])
            aux = aux - 1
        for i in range(0, 3):
            diag.append(board[i][i])
        if all(e == t for e in diag): # check main diagonal
                return t
        if all(e == t for e in diag2): # check secondary diagonal
            return t
    return None


# Returns True if game is over, False otherwise.
def terminal(board):
    if count_empty(board) == 0 or winner(board) != None:
        return True
    return False


# Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
def utility(board):
    r = winner(board)
    if r == X:
        return 1
    elif r == O:
        return -1
    else:
        return 0

def maxvalue(board):
    #aux = copy.deepcopy(board)
    if terminal(board):
        return utility(board)
    v = -1
    for a in actions(board):
        r = minvalue(result(board, a))
        v = max(v, r)
        if v == 1:
            break
    return v

def minvalue(board):
    #aux = copy.deepcopy(board)
    if terminal(board):
        return utility(board)
    v = 1
    for a in actions(board):
        r = maxvalue(result(board, a))
        v = min(v, r)
        if v == -1:
            break
    return v

# Returns the optimal action for the current player on the board.
def minimax(board):
    if terminal(board):
        return None
    if get_letter(board) == X:
        best = -1
        move = (-1, -1)
        if count_empty(board) == 0:
            return move
        for action in actions(board):
            move_value = minvalue(result(board, action))
            if move_value == 1:
                move = action
                break
            if move_value > best: #alpha beta pruning
                move = action
        return move # X aims to maximize score
    else:
        best = 1
        move = (-1, -1)
        for action in actions(board):
            move_value = maxvalue(result(board, action))
            if move_value == -1:
                move = action
                break
            if move_value < best: #alpha beta pruning
                move = action
        return move # O aims to minimize score