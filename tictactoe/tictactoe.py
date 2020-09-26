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
            
# Returns set of all possible actions (i, j) available on the board.
"""
def actions(board):
    possibles = []
    for i in range (0, 3):
        for j in range(0, 3):
            aux = copy.deepcopy(board)
            if board[i][j] == None:
                aux[i][j] = ROUND
                possibles.append(aux)
    return possibles
"""

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
    board[action[0]][action[1]] = get_letter(board)
    return board

# Returns the board that results from making move (i, j) on the board.
def resultAux(board, action):
    board[action[1][0]][action[1][1]] = get_letter(board)
    return board


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
    return False if utility(board) == 0 else True


# Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
def utility(board):
    turn = [X, O]
    for t in turn:
        diag2 = []
        aux = 2 # aux for secondary diagonal
        result = 1 if t == X else -1
        for i in range (0, 3):
            if all(e == t for e in board[i]):
                return result
            col = []
            diag = []
            for j in range (0, 3):
                col.append(board[j][i])
                diag.append(board[i][j])
            if all(e == t for e in col): # check elements per column
                return result
            diag2.append(board[i][aux])
            aux = aux - 1
        if all(e == t for e in diag): # check main diagonal
                return result
        if all(e == t for e in diag2): # check secondary diagonal5
            return result
    return 0

def maxvalue(board, v):
    if terminal(board):
        return [utility(board), (v[1])]
    for a in actions(board):
        v[1] = a
        r = minvalue(resultAux(board, v), v)
        v[0] = max(v[0], r[0])
    return v

def minvalue(board, v):
    if terminal(board):
        return [utility(board), (v[1])]
    for a in actions(board):
        v[1] = a
        r = maxvalue(resultAux(board, v), v)
        v[0] = min(v[0], r[0])
    return v

# Returns the optimal action for the current player on the board.
def minimax(board):
    if get_letter(board) == X:
        v = [-2, (0,0)]
        r = maxvalue(board, v)
        return r[1] # X aims to maximize score
    else:
        v = [2, (0,0)]
        r = minvalue(board, v)
        print(r)
        return r[1] # O aims to minimize
