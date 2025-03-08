class Piece:
    def __init__(self, color, pos, board): ##color(black  or white inkl direction too**
        self.color = color
        self.pos = pos
        self.board = board
        
    def get_pos(self):
        return self.pos
    
    def set_pos(self,new_pos):
        self.pos = new_pos

    #check whether it is a capture or not
    def is_capture(self, new_pos):
        x1, y1 = self.pos
        x2, y2 = new_pos

       
        if not self.is_valid(new_pos):
            return False

        target = self.board[x2][y2]
        
        
        if target is None :
            return False  
        
        if target.color != self.color:
            return True  
        
        return False  

    #create a copy of the piece:
    def copy_piece(self):
        return self.__class__(self.color , self.pos, self.board)

class Pawn(Piece):
    def __init__(self, color, pos, board):
        super().__init__(color, pos, board)

    def is_valid(self, new_pos):
        x1, y1 = self.pos
        x2, y2 = new_pos
        if self.color == "w":
            dir = -1
            start = 6
        else:
            dir = 1
            start = 1
       
        ##forward 1##
        if y1 == y2 and x2 == x1 + dir and self.board[x2][y2] is None:
            return True
        
        ##capture diagonally##
        if y2 - y1 in (-1, 1) and x2 == x1 + dir:
            target = self.board[x2][y2] 
            if target is not None and target.color != self.color:
                return True
        
        ##forward 2##    
        if x2 == x1 + 2 * dir and y1 == y2 and x1 == start and self.board[x1 + dir][y1] is None and self.board[x2][y2] is None and start == x1 :
            return True

        #any invalid#
        return False
     
            
        
class King(Piece):
    def __init__(self, color, pos, board):
        super().__init__(color, pos, board)
    
    def is_valid(self, new_pos):
        x1, y1 = self.pos
        x2, y2 = new_pos
       #check target#
        target = self.board[x2][y2]
        if target is not None and target.color == self.color:
            return False

        dx = abs(x2 - x1)
        dy = abs(y2 - y1)

        if dx <= 1 and dy <= 1:
            return True
        
        return False

        
class Queen(Piece):
    def __init__(self, color, pos, board):
        super().__init__(color, pos, board)

    def is_valid(self, new_pos):  
        x1, y1 = self.pos
        x2, y2 = new_pos

        # Check target
        target = self.board[x2][y2]
        if target and target.color == self.color:
            return False

        #if vertical or horizontal (just like rook)#
        if y1 == y2 or x1 == x2:
            # Horizontal movement
            if y1 == y2:
                if x2 > x1:
                    step = 1
                else:
                    step = -1
                for x in range(x1 + step, x2, step):
                    if self.board[x][y1] is not None:
                        return False
            # Vertical movement
            else:
                if y2 > y1:
                    step = 1
                else:
                    step = -1
                for y in range(y1 + step, y2, step):
                    if self.board[x1][y] is not None:
                        return False
            return True

        # if horizontal
        dx = abs(x2 - x1)
        dy = abs(y2 - y1)
        if dx != dy:
            return False  # Not diagonal
        #check path#
        if x2 > x1:
            x_step = 1
        else:
            x_step = -1
        if y2 > y1:
            y_step = 1
        else:
            y_step = -1
        
        for i in range(1, dx):
            check_x = x1 + i * x_step
            check_y = y1 + i * y_step
            if self.board[check_x][check_y] is not None:
                return False
        return True

class Knight(Piece):
    def __init__(self, color, pos, board):
        super().__init__(color, pos, board)
        

    def is_valid(self, new_pos):
        x1, y1 = self.pos
        x2, y2 = new_pos
       #check target#
        target = self.board[x2][y2]
        if target is not None and target.color == self.color:
            return False
            
        dx = abs(x2 - x1)
        dy = abs(y2 - y1)
        
        if (dx == 1 and dy == 2) or (dx == 2 and dy == 1):
            return True

        return False

class Bishop(Piece):
    def __init__(self, color, pos, board):
        super().__init__(color, pos, board)

    def is_valid(self, new_pos):
        x1, y1 = self.pos
        x2, y2 = new_pos
       #check target#
        target = self.board[x2][y2]
        if target is not None and target.color == self.color:
            return False
    
        #check if diagonal#
        dx = abs(x2 - x1)
        dy = abs(y2 - y1)
        #if the diff is different then its not diagonal#
        if dx != dy or dx == 0 or dy == 0:
            return False

        #check path#
        if x2 > x1:
            x_step = 1
        else:
            x_step = -1
        if y2 > y1:
            y_step = 1
        else:
            y_step = -1

        for i in range(1, dx):
            checkx = x1 + i * x_step
            checky = y1 + i * y_step
            if self.board[checkx][checky] is not None:
                return False
        return True

class Rook(Piece):
    def __init__(self, color, pos, board):
        super().__init__(color, pos, board)
        
    def is_valid(self, new_pos):
        x1, y1 = self.pos
        x2, y2 = new_pos

        #check target#
        target = self.board[x2][y2]
        if target is not None and target.color == self.color:
            return False

        #check if the path is clear or not#
        if y1 == y2:
            if x2 > x1:
                step = 1
            else:
                step = -1
            for x in range(x1 + step, x2, step):
                if self.board[x][y1] is not None:
                    return False
                
            return True
        if x1 == x2:
            if y2 > y1:
                step = 1
            else:
                step = -1
            for y in range(y1 + step, y2, step):
                if self.board[x1][y] is not None:
                    return False
                    
            return True

        #any invalid moves#
        return False


   
        