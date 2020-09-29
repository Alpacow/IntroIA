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
    return len([e for listL in board for e in listL if e is None])
    

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
            if board[i][j] == None:
                possibles.append((i,j))
    return possibles

# Returns the board that results from making move (i, j) on the board.
def result(board, action):
    aux = copy.deepcopy(board)
    if action[0] >= 0 and action[0] <=2 and action[1] >= 0 and action[1] <= 2:
        aux[action[0]][action[1]] = get_letter(board)
        return aux
    else:
        raise Exception("Index out of range")

# Returns the winner of the game, if there is one.
def winner(board):
    r = utility(board)
    if r == 1:
        return X
    elif r == -1:
        return O
    else:
        return None


# Returns True if game is over, False otherwise.
def terminal(board):
    return False if winner(board) == None and count_empty(board) != 0 else True


# Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
def utility(board):
    turn = [X, O]
    for t in turn:
        diag2 = []
        aux = 2 # aux for secondary diagonal
        result = 1 if t == X else -1
        for i in range (0, 3): # check elements per line
            if all(e == t for e in board[i]):
                return result
            col = []
            diag = []
            for j in range (0, 3):
                col.append(board[j][i])
            if all(e == t for e in col): # check elements per column
                return result
            diag2.append(board[i][aux])
            aux = aux - 1
        for i in range(0, 3):
            diag.append(board[i][i])
        if all(e == t for e in diag): # check main diagonal
                return result
        if all(e == t for e in diag2): # check secondary diagonal5
            return result
    return 0

def maxvalue(board, v):
    #aux = copy.deepcopy(board)
    if terminal(board):
        return [utility(board), (v[1])]
    for a in actions(board):
        v[1] = a
        r = minvalue(result(board, a), v)
        v[0] = max(v[0], r[0])
    return v

def minvalue(board, v):
    #aux = copy.deepcopy(board)
    if terminal(board):
        return [utility(board), (v[1])]
    for a in actions(board):
        v[1] = a
        r = maxvalue(result(board, a), v)
        v[0] = min(v[0], r[0])
    return v

# Returns the optimal action for the current player on the board.
def minimax(board):
    print("\n*************************************************** ENTROU MINMAX *************************************\n")
    if terminal(board):
        return None
    if get_letter(board) == X:
        v = [-math.inf, (0,0)]
        r = maxvalue(board, v)
        print("X maximizou para ", r)
        return r[1] # X aims to maximize score
    else:
        v = [math.inf, (0,0)]
        r = minvalue(board, v)
        print("O minimizou para ", r)
        return r[1] # O aims to minimize

"""
        if r[0] >= 2: # 2 is beta value
            return v
        if r[0] > v[0]:
            v[0] = r[0]
"""