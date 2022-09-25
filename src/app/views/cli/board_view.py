from dataclasses import dataclass, field
from app.models.board import Board
from app.models.postition import Position
from app.views.cli.view import View

@dataclass
class BoardView(View):
    board: Board
    
    def print(self):
        print(self.title)
        current_row: int = 0
        for position,tile in self.board.tiles.items():
            if position.y > current_row:
                print()
                current_row = position.y
            self.print_tile(position)
        print()
        
    def print_tile(self, position: Position) -> None:
        print(self.board[position], end="")