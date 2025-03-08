from algoviz import AlgoViz
from algoviz.svg import Rect, Circle, Text, RGBAColor, SVGView, Path
from board import Board
from piece import Piece, Rook, Knight, Bishop, Queen, King, Pawn
from piecedrawer import PieceDrawer
import time as t

# Colors
WHITE_TILE = RGBAColor(248, 231, 187)
BLACK_TILE = RGBAColor(242, 202, 92)
WHITE_PIECE = RGBAColor(255, 255, 255)
BLACK_PIECE = RGBAColor(0, 0, 0)
HIGHLIGHT_COLOR = RGBAColor(50, 205, 50, 150)
 

class Player:
    def __init__(self, name, color, captured_pieces):
        self.name = name
        self.color = color
        self.captured_pieces = captured_pieces

class Game:
    def __init__(self):
        self.drawing = SVGView(700, 500, "Chess")  # Wider view for captured pieces
        self.board = Board()
        self.tile_size = 50
        self.tiles = []
        self.piece_visuals = {}
        self.move_indicators = []
        self.captured_visuals = []
        self.current_player = 'w'
        self.old_current_player = self.current_player #used for the timer
        self.players = []
        self.name_white = input("Enter white player's name: ")
        self.name_black = input("Enter black player's name: ")
        #timer initial variables (obsolete)
        """self.time_limit = int(input("Enter how much time per player (in seconds):"))
        self.still_time = True
        self.start_time = t.time()
        self.timer_text = "00:00"
        self.timer1 = Text(self.timer_text, 500, 0, self.drawing)
        self.timer2 = Text(self.timer_text, 500, 350, self.drawing)
        self.time_diff = 0
        self.white_time = self.time_limit
        self.black_time = self.time_limit """
        self.selected_piece = None
        self.piece_drawer = PieceDrawer(self.drawing)
        self.init_players()
        self.init_board()
        

    def init_players(self):
        # White captures black pieces, Black captures white pieces
        self.white_player = Player(self.name_white, 'w', self.board.black_captured_pieces)
        self.black_player = Player(self.name_black, 'b', self.board.white_captured_pieces)
        self.players = [self.white_player, self.black_player]

    def init_board(self):
        # Draw chessboard tiles
        for i in range(8):
            self.tiles.append([])
            for j in range(8):
                color = BLACK_TILE if (i + j) % 2 else WHITE_TILE
                tile = Rect(j * self.tile_size, i * self.tile_size, 
                            self.tile_size, self.tile_size, self.drawing)
                tile.set_fill(color)
                self.tiles[i].append(tile)
        self.draw_pieces()

        #draw 1 - 8 on the side of the board
        for i in range(8):
            rank_label = Text(str(8 - i), 8 * self.tile_size + 5, i * self.tile_size + 30, self.drawing)
        #draw a - h on the bottom
        for j in range(8):
            file_label = Text(chr(97 + j), j * self.tile_size + 20, 8 * self.tile_size + 15, self.drawing)

    def draw_pieces(self):
        """Draw all pieces on the board."""
        # Clear existing pieces
        for visual in self.piece_visuals.values():
            visual.remove()
        self.piece_visuals.clear()
    
        # Draw new pieces
        for i in range(8):
            for j in range(8):
                piece = self.board.board[i][j]
                if piece:
                    x, y = j * self.tile_size + 25, i * self.tile_size + 25
                    color = WHITE_PIECE if piece.color == "w" else BLACK_PIECE
    
                    # Use the correct drawing function based on the piece type
                    if isinstance(piece, Pawn):
                        visuals = self.piece_drawer.draw_pawn(x, y, color)
                    elif isinstance(piece, Rook):
                        visuals = self.piece_drawer.draw_rook(x, y, color)
                    elif isinstance(piece, Knight):
                        visuals = self.piece_drawer.draw_knight(x, y, color)
                    elif isinstance(piece, Bishop):
                        visuals = self.piece_drawer.draw_bishop(x, y, color)
                    elif isinstance(piece, Queen):
                        visuals = self.piece_drawer.draw_queen(x, y, color)
                    elif isinstance(piece, King):
                        visuals = self.piece_drawer.draw_king(x, y, color)

                    self.piece_visuals[(i, j)] = visuals

    
    def draw_captured_pieces(self):
    # Clear previous captured visuals
        for visual in self.captured_visuals:
            visual.remove()
        self.captured_visuals.clear()
    
        # Positioning parameters
        x_start = 450
        y_start_white = 250
        y_start_black = 50
        spacing = 40  # Space between captured pieces
    
        # Draw white player's captured pieces (black pieces)
        for i, piece in enumerate(self.white_player.captured_pieces):
            x = x_start + (i % 4) * spacing
            y = y_start_white + (i // 4) * spacing
            color = BLACK_PIECE  # Captured black pieces
            
            # Get the appropriate piece visuals
            if isinstance(piece, Pawn):
                visuals = self.piece_drawer.draw_pawn(x, y, color)
            elif isinstance(piece, Rook):
                visuals = self.piece_drawer.draw_rook(x, y, color)
            elif isinstance(piece, Knight):
                visuals = self.piece_drawer.draw_knight(x, y, color)
            elif isinstance(piece, Bishop):
                visuals = self.piece_drawer.draw_bishop(x, y, color)
            elif isinstance(piece, Queen):
                visuals = self.piece_drawer.draw_queen(x, y, color)
            elif isinstance(piece, King):
                visuals = self.piece_drawer.draw_king(x, y, color)
                
            self.captured_visuals.append(visuals)
    
        # Draw black player's captured pieces (white pieces)
        for i, piece in enumerate(self.black_player.captured_pieces):
            
            x = x_start + (i % 4) * spacing
            y = y_start_black + (i // 4) * spacing
            color = WHITE_PIECE  # Captured white pieces
            
            # Get the appropriate piece visuals
            if isinstance(piece, Pawn):
                visuals = self.piece_drawer.draw_pawn(x, y, color)
            elif isinstance(piece, Rook):
                visuals = self.piece_drawer.draw_rook(x, y, color)
            elif isinstance(piece, Knight):
                visuals = self.piece_drawer.draw_knight(x, y, color)
            elif isinstance(piece, Bishop):
                visuals = self.piece_drawer.draw_bishop(x, y, color)
            elif isinstance(piece, Queen):
                visuals = self.piece_drawer.draw_queen(x, y, color)
            elif isinstance(piece, King):
                visuals = self.piece_drawer.draw_king(x, y, color)
                
            self.captured_visuals.append(visuals) 

    def display_moves(self, piece):  # Renamed for clarity
        self.clear_move_indicators()
        valid_moves = self.board.show_available_moves(piece)  # No need to filter again!
        
        for x, y in valid_moves:
            indicator = Circle(y * self.tile_size + 25, x * self.tile_size + 25, 
                               10, self.drawing)
            indicator.set_fill(HIGHLIGHT_COLOR)
            self.move_indicators.append(indicator)
        
        return valid_moves  # Just return what Board already calculated


    def clear_move_indicators(self):
        for indicator in self.move_indicators:
            indicator.remove()
        self.move_indicators.clear()

    def run_timer(self): #code is not run
        if self.current_player != self.old_current_player:
            if self.current_player == 'w':
                self.black_time = self.white_time - self.time_diff
                self.timer_text = "00:{}".format(int(round(self.white_time)))
                self.timer2.set_text(self.timer_text)
                self.old_current_player = self.current_player
            elif self.current_player == 'b':
                self.white_time = self.white_time - self.time_diff
                self.timer_text = "00:{}".format(int(round(self.black_time)))
                self.timer1.set_text(self.timer_text)
                self.old_current_player = self.current_player
            self.start_time = t.time()
            current_time = self.start_time
            time_diff = 0
            old_time_diff = 0
        current_time = t.time()
        time_diff = current_time - self.start_time
        if int(round(self.time_limit-time_diff)) < 10:
            self.timer_text = "00:0{}".format(int(round(self.time_limit-time_diff)))
        else:
            self.timer_text = "00:{}".format(int(round(self.time_limit-time_diff)))
        self.timer.set_text(self.timer_text)
        if int(round(time_diff)) >= self.time_limit:
            self.still_time = False

    def run(self):
        while True:
            pieces_left = 0
            for x in range(8):
                for y in range(8):
                    if self.board.board[x][y] != None:
                        pieces_left += 1

            if pieces_left == 2:
                print("Draw by insufficient material")
                        
            
            #self.run_timer() #works in theory but in practise the timer only updates whenever wait_for_click() is not running, leading to it looking unsatisfying, so we removed it
            if not self.board.has_legal_moves(self.current_player):
                king = self.board.get_king_by_color(self.current_player)
                if king and self.board.is_check(self.current_player):
                    if self.current_player == "w":
                        print(f"Checkmate! {self.name_white} loses.")
                    else:
                        print(f"Checkmate! {self.name_black} loses.") 
                else:
                    print("Stalemate! It's a draw.")
                break

            click = self.drawing.wait_for_click()
            true_x = int(click.x() / self.tile_size)
            true_y = int(click.y() / self.tile_size)

            if not (0 <= true_x < 8 and 0 <= true_y < 8):
                
                continue

            if click.buttons() == 0:  # Left-click
                clicked_piece = self.board.board[true_y][true_x]

                if self.selected_piece is None:
                    if clicked_piece and clicked_piece.color == self.current_player:
                        legal_moves = self.display_moves(clicked_piece)
                        if legal_moves:
                            self.selected_piece = clicked_piece
                        else:
                            self.clear_move_indicators()
                else:
                    if (true_y, true_x) in self.display_moves(self.selected_piece):
                        success = self.board.move_piece(self.selected_piece, (true_y, true_x))
                        if success:
                            if self.current_player == "w":
                                print(self.name_white, self.board.conversion(self.selected_piece))
                                self.draw_pieces()
                                self.draw_captured_pieces()
                                self.current_player = "b" 
                        
                            else:
                                print(self.name_black, self.board.conversion(self.selected_piece))
                                self.draw_pieces()
                                self.draw_captured_pieces()
                                self.current_player = "w" 
                    self.selected_piece = None
                    self.clear_move_indicators()

            elif click.buttons() == 2:  # Right-click (Cancel)
                self.selected_piece = None
                self.clear_move_indicators()