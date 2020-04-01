'''
Author: Eric P. Nichols
Date: Feb 8, 2008.
Board class.
Board data:
  1=white, -1=black, 0=empty
  first dim is column , 2nd is row:
     pieces[1][7] is the square in column 2,
     at the opposite end of the board in row 8.
Squares are stored and manipulated as (x,y) tuples.
x is the column, y is the row.
'''
class Board():


    def __init__(self, n):
        "Set up initial board configuration."

        self.n = n
        self.colors = ['2','3','4']
        self.pieces = [ 
            [0, 1, 0, 0, 0, 0, 0, 0, 0, 1 ],
            [1, 0, 1, 0, 0, 0, 0, 1, 0, 0 ],
            [0, 1, 0, 1, 0, 0, 0, 0, 0, 0 ],
            [0, 0, 1, 0, 1, 1, 0, 0, 0, 0 ],
            [0, 0, 0, 1, 0, 1, 0, 0, 0, 0 ],
            [0, 0, 0, 1, 1, 0, 1, 0, 0, 0 ],
            [0, 0, 0, 0, 0, 1, 0, 1, 0, 0 ],
            [0, 1, 0, 0, 0, 0, 1, 0, 1, 0 ],
            [0, 0, 0, 0, 0, 0, 0, 1, 0, 1 ],
            [1, 0, 0, 0, 0, 0, 0, 0, 1, 0 ],
        ]
        self.action_dict = dict()
        count = 0
        for i in range(self.n):
            for j in range(self.n):
                for co in self.colors:
                    self.action_dict[count] = ((i, j), co)
                    count += 1
        self.action_dict_inv = {v: k for k, v in self.action_dict.items()}
    '''
    # add [][] indexer syntax to the Board
    def __getitem__(self, index): 
        return self.pieces[index]


    '''
    def get_legal_moves(self, color):
        """Returns all the legal moves for the given color.
        (1 for white, -1 for black
        """
        moves = list()  # stores the legal moves.

        # Get all the squares with pieces of the given color.        
        for y in range(self.n):
            for x in range(y):
                if self.pieces[x][y]==1:
                    newmoves = self.get_moves_for_square((x,y))
                    moves += newmoves

        return moves

    def has_legal_moves(self):

        for y in range(self.n):
            for x in range(y):
                if self.pieces[x][y]==1:
                    newmoves = self.get_moves_for_square((x,y))
                    if len(newmoves)>0:
                        return True
        return False

    def get_moves_for_square(self, square):
        """Returns all the legal moves that use the given square as a base.
        That is, if the given square is (3,4) and it contains a black piece,
        and (3,5) and (3,6) contain white pieces, and (3,7) is empty, one
        of the returned moves is (3,7) because everything from there to (3,4)
        is flipped.
        """
        moves = []
        valid_colors = list(self.colors)

        for node in square:
            for idx, co in enumerate(self.pieces[node]):
                if idx in square:
                    continue #pass this edge
                if co in valid_colors:
                    valid_colors.remove(co)
        
        for c in valid_colors:
            moves.append((square,c))

        # return the generated move list
        return moves

    def execute_move(self, move):
        """Perform the given move on the board; flips pieces as necessary.
        color gives the color pf the piece to play (1=white,-1=black)
        """

        #Much like move generation, start at the new piece's square and
        #follow it on all 8 directions to look for a piece allowing flipping.

        # Add the piece to the empty square.
        # print(move)
        move = self.action_dict[move]
        self.pieces[move[0][0]][move[0][1]] = move[1]
        self.pieces[move[0][1]][move[0][0]] = move[1]

'''
    def _get_flips(self, origin, direction, color):
        """ Gets the list of flips for a vertex and direction to use with the
        execute_move function """
        #initialize variables
        flips = [origin]

        for x, y in Board._increment_move(origin, direction, self.n):
            #print(x,y)
            if self[x][y] == 0:
                return []
            if self[x][y] == -color:
                flips.append((x, y))
            elif self[x][y] == color and len(flips) > 0:
                #print(flips)
                return flips

        return []

    @staticmethod
    def _increment_move(move, direction, n):
        # print(move)
        """ Generator expression for incrementing moves """
        move = list(map(sum, zip(move, direction)))
        #move = (move[0]+direction[0], move[1]+direction[1])
        while all(map(lambda x: 0 <= x < n, move)): 
        #while 0<=move[0] and move[0]<n and 0<=move[1] and move[1]<n:
            yield move
            move=list(map(sum,zip(move,direction)))
            #move = (move[0]+direction[0],move[1]+direction[1])

'''