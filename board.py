from piece import Piece, Rook, King, Pawn, Bishop, Knight, Queen

class Board:
    def __init__(self, add_pieces=True):
        self.board =[[None for i in range(8)] for i in range(8)]
        self.white_captured_pieces = []  
        self.black_captured_pieces = []
        if add_pieces:
            self.add_pieces()
        

    def add_pieces(self):
        for i in range(8):
            self.board[1][i] = Pawn("b", (1, i), self.board)  # Black pawns
            self.board[6][i] = Pawn("w", (6, i), self.board)  # White pawns

        # Setup rooks
        self.board[0][0] = Rook("b", (0, 0), self.board)
        self.board[0][7] = Rook("b", (0, 7), self.board)
        self.board[7][0] = Rook("w", (7, 0), self.board)
        self.board[7][7] = Rook("w", (7, 7), self.board)

        # Setup knights
        self.board[0][1] = Knight("b", (0, 1), self.board)
        self.board[0][6] = Knight("b", (0, 6), self.board)
        self.board[7][1] = Knight("w", (7, 1), self.board)
        self.board[7][6] = Knight("w", (7, 6), self.board)

        # Setup bishops
        self.board[0][2] = Bishop("b", (0, 2), self.board)
        self.board[0][5] = Bishop("b", (0, 5), self.board)
        self.board[7][2] = Bishop("w", (7, 2), self.board)
        self.board[7][5] = Bishop("w", (7, 5), self.board)

        # Setup queens
        self.board[0][3] = Queen("b", (0, 3), self.board)
        self.board[7][3] = Queen("w", (7, 3), self.board)

        # Setup kings
        self.board[0][4] = King("b", (0, 4), self.board)
        self.board[7][4] = King("w", (7, 4), self.board)

    # In Board class
    def get_king_by_color(self, color):
        for x in range(8):
            for y in range(8):
                piece = self.board[x][y]
                if isinstance(piece, King) and piece.color == color:
                    return (x, y)
        return None

    def is_check(self, color):
        king_pos = self.get_king_by_color(color)
        if king_pos is None:
            return False  # No king found (shouldn't happen in normal games)
        
        xk, yk = king_pos
        for x in range(8):
            for y in range(8):
                piece = self.board[x][y]
                if piece is not None and piece.color != color:
                    if piece.is_valid(king_pos):  # Can this piece attack the king?
                        return True  # King is in check!
        
        return False  # No threats to the king
    
        
            # Restore the king
        self.board[xk][yk] = original_king
        return in_check
    def move_piece(self, piece, new_pos):
        x1, y1 = piece.pos
        x2, y2 = new_pos
    
        if not piece.is_valid(new_pos):
            return False
    
        # Simulate move on copied board
        check_board = self.copy_board()
        check_piece = check_board.board[x1][y1]
        
    
        check_board.board[x1][y1] = None
        check_board.board[x2][y2] = check_piece
        check_piece.set_pos((x2, y2))
    
        # Check if the move leaves the king in check (use piece.color)
        if check_board.is_check(piece.color):
            return False
    
        # Execute the move on the real board
        target = self.board[x2][y2]
        
        if isinstance(target, King):
            return False
            
        if target is not None:
            if target.color == 'w':
                self.white_captured_pieces.append(target)
            else:
                self.black_captured_pieces.append(target)
    
        self.board[x1][y1] = None
        self.board[x2][y2] = piece
        piece.set_pos(new_pos)
        return True

    def has_legal_moves(self, color):
        for x in range(8):
            for y in range(8):
                test_piece = self.board[x][y]
                if test_piece is not None and test_piece.color == color:
                    for x1 in range(8):
                        for y1 in range(8):
                            if test_piece.is_valid((x1, y1)):
                                check_board = self.copy_board()
                                check_piece = check_board.board[x][y]
                                if check_piece is None:
                                    continue
    
                                # Manually apply the move
                                check_board.board[x][y] = None
                                check_board.board[x1][y1] = check_piece
                                check_piece.set_pos((x1, y1))
    
                                if not check_board.is_check(color):
                                    return True
        return False

    #showing available moves
    def show_available_moves(self, piece):
        available_moves = []
        x1, y1 = piece.pos
    
        for x2 in range(8):
            for y2 in range(8):
                if piece.is_valid((x2, y2)):
                    
                    target = self.board[x2][y2]
                    if isinstance(target, King):
                        continue
                        
                    check_board = self.copy_board()
                    check_piece = check_board.board[x1][y1]
                    if check_piece is None:
                        continue
    
                    # Manually apply the move
                    check_board.board[x1][y1] = None
                    check_board.board[x2][y2] = check_piece
                    check_piece.set_pos((x2, y2))
    
                    # Check if the king is safe after the move
                    if not check_board.is_check(piece.color):
                        available_moves.append((x2, y2))
    
        return available_moves

    #convert pos to chess notation (for display)
    def conversion(self, piece):
        x, y = piece.pos
        xNot = 8 - x
        yNot = chr(97 + y)
        chessNot = ""
        if isinstance(piece, Pawn):
            chessNot = yNot  + str(xNot)
        elif isinstance(piece, Rook):
            chessNot = "R" + yNot  + str(xNot)
        elif isinstance(piece, Bishop):
            chessNot = "B" + yNot  + str(xNot)
        elif isinstance(piece, King):
            chessNot = "K" + yNot  + str(xNot)
        elif isinstance(piece, Queen):
            chessNot = "Q" + yNot  + str(xNot)
        elif isinstance(piece, Knight):
            chessNot = "N" + yNot  + str(xNot)            
        return chessNot    

    #to simulate the board
    def copy_board(self):
        new_board = Board(add_pieces=False)
        
        for x in range(8):
            for y in range(8):
                piece = self.board[x][y]
                if piece is not None:
                    new_piece = piece.copy_piece()
                    new_piece.board = new_board.board
                    new_board.board[x][y] = new_piece
        return new_board

    #check whether any moves are available to escape from check
    def checkmate(self, color):
        return self.is_check(color) and not self.has_legal_moves(color)

    def stalemate(self, color):
        return (not self.is_check(color)) and (not self.has_legal_moves(color))

    




       

    