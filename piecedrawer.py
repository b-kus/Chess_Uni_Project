from algoviz import AlgoViz
from algoviz.svg import Rect, Circle, Text, RGBAColor, SVGView, Path

class PieceDrawer:
    def __init__(self, drawing):
        self.drawing = drawing

    def draw_pawn(self, x, y, color):
        
        body_path = f"M {x-5} {y-15} L {x+5} {y-15} L {x+5} {y-5} L {x+3} {y-5} L {x+10} {y+15} L {x-10} {y+15} L {x-3} {y-5} L {x-5} {y-5} Z"  
        body = Path(body_path, self.drawing)
        body.set_fill(color)
    
        return body
    
    def draw_rook(self, x, y, color):
        
    
        
        body_path = f"M {x - 8} {y+15} L {x+8} {y+15} L {x + 5} {y-5} L {x + 8} {y - 5} L {x +8} {y - 15} L {x + 5} {y - 15} L {x + 5 } {y - 10} L {x +1} {y - 10} L {x+1} {y - 15} L {x-1} {y - 15} L {x - 1} {y - 10} L {x - 5} {y - 10} L {x - 5} {y - 10} L {x - 5} {y - 15} L {x - 8} {y - 15} L {x - 8} {y -10} L {x - 8 } {y -5} L {x - 5} { y -5} Z"  
        body = Path(body_path, self.drawing)
        body.set_fill(color)
    
        return body
    
    def draw_queen(self, x, y, color):
        
        
        body_path = f"M {x - 15} {y-15} L {x-5} {y} L {x} {y-15} L {x +5} {y} L {x + 15} {y - 15} L {x+15} {y + 15} L {x - 15} {y+15} Z"  
        body = Path(body_path, self.drawing)
        body.set_fill(color)
    
        return body
    
    def draw_knight(self, x, y, color):
        
        body_path = f"M {x - 10} {y+15} L {x+10} {y + 15} L {x + 5} {y-15} L {x -5} {y - 15} L {x - 10} {y -5} L{x -10} {y} L {x-5} {y-5} Z"  
        body = Path(body_path, self.drawing)
        body.set_fill(color)
    
        return body
    
    def draw_king(self, x, y, color):
        
        body_path = f"M {x - 15} {y+15} L {x+15} {y + 15} L {x + 15} {y-15} L {x +5} {y + 5} L {x + 2} {y +5} L{x +2} {y -5} L {x+5} {y-5} L {x+5} {y-8} L {x + 2} {y - 8} L {x +2} {y -15} L {x-2} {y -15} L {x-2} {y - 8} L {x-5} {y -8} L {x-5} { y-5} L {x-2} {y-5} L {x-2} {y +5} L {x-5} {y+5} L {x-15} {y -15} Z"  
        body = Path(body_path, self.drawing)
        body.set_fill(color)
    
        return body
    
    def draw_bishop(self, x, y, color):
        
        #  (Body) using Path
        body_path = f"M {x - 10} {y+15} L {x+10} {y + 15} L {x + 2} {y-5} L {x +5} {y - 15} L {x} {y -20} L{x -5} {y-15} L {x-2} {y-5} Z"  
        body = Path(body_path, self.drawing)
        body.set_fill(color)
    
        return body

