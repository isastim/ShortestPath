from dataclasses import dataclass, field
from typing import List
from app.models.board import Board
from app.models.postition import Position
from app.views.cli.board_view import BoardView
from app.views.cli.view import View

@dataclass
class PositionView(BoardView):
    positions: List[Position]
    
    def print_tile(self, position: Position) -> None:
        print(self.board[position] if position not in self.positions else "[O]", end="")