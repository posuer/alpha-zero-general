from __future__ import print_function
import sys
sys.path.append('..')
from Game import Game
from .GraphcolorLogic import Board
import numpy as np

class GraphcolorGame(Game):
    square_content = {
        1: "-",
        2: "R",
        3: "Y",
        4: "G"
    }

    @staticmethod
    def getSquarePiece(piece):
        return GraphcolorGame.square_content[piece]

    def __init__(self, n):
        self.n = n

    def getInitBoard(self):
        # return initial board (numpy board)
        b = Board(self.n)
        return np.array(b.pieces)

    def getBoardSize(self):
        # (a,b) tuple
        return (self.n, self.n) 

    def getActionSize(self):
        # return number of actions
        return self.n*self.n*3 + 1

    def getNextState(self, board, player, action):
        # if player takes action on board, return next (board,player)
        # action must be a valid move
        if action == self.n*self.n:
            return (board, -player)

        b = Board(self.n)
        b.pieces = np.copy(board)
        #move = (int(action/self.n), action%self.n)
        move = b.action_dict[action]
        b.execute_move(action)
        return (b.pieces, -player)

    def getValidMoves(self, board, player):
        # return a fixed size binary vector
        valids = [0 for i in range(self.getActionSize()) ]
        b = Board(self.n)
        b.pieces = np.copy(board)
        legalMoves =  b.get_legal_moves(player)
        if len(legalMoves)==0:
            valids[-1]=1
            return np.array(valids)
        for key in legalMoves:
            valids[b.action_dict_inv[key]]=1
        return np.array(valids)

    def getGameEnded(self, board, player):
        # return 0 if not ended, 1 if player 1 won, -1 if player 1 lost
        # player = 1
        b = Board(self.n)
        b.pieces = np.copy(board)
        if b.has_legal_moves():
            return 0
        return 1
    
    def getCanonicalForm(self, board, player):
        # return state if player==1, else return -state if player==-1
        return board#player*board
    '''
    def getSymmetries(self, board, pi):
        # mirror, rotational
        assert(len(pi) == self.n**2+1)  # 1 for pass
        pi_board = np.reshape(pi[:-1], (self.n, self.n))
        l = []

        for i in range(1, 5):
            for j in [True, False]:
                newB = np.rot90(board, i)
                newPi = np.rot90(pi_board, i)
                if j:
                    newB = np.fliplr(newB)
                    newPi = np.fliplr(newPi)
                l += [(newB, list(newPi.ravel()) + [pi[-1]])]
        return l
    '''
    def stringRepresentation(self, board):
        return board.tostring()

    def stringRepresentationReadable(self, board):
        board_s = "".join(self.square_content[square] for row in board for square in row)
        return board_s

    def getScore(self, board, player):

        return np.count_nonzero(board > 1) 

    @staticmethod
    def display(board):
        n = board.shape[0]
        print("   ", end="")
        for y in range(n):
            print(y, end=" ")
        print("")
        print("-----------------------")
        for y in range(n):
            print(y, "|", end="")    # print the row #
            for x in range(n):
                piece = board[y][x]    # get the piece to print
                print(GraphcolorGame.square_content[piece], end=" ")
            print("|")

        print("-----------------------")
