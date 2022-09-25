from dataclasses import dataclass, field
from app.models.adjacent import Adjacent
from app.models.board import Board
from app.models.position_factory import PositionFactory
from app.models.postition import Position
from app.models.tile import Tile
from app.views.cli.board_view import BoardView

@dataclass
class BoardController:
    board: Board = field(default_factory=lambda: Board(2,2))
    
    def get_tile(self, position: Position) -> Tile:
        self.board[position]
    
    def set_tile(self, position: Position, tile: Tile) -> None:
        self.board[position] = tile
    
    def get_adjacent_tiles(self, position: Position) -> Adjacent[Tile]:
        adjacent_positions: Adjacent[Position] = PositionFactory.get_adjacent_positions(position, self.board)
        return Adjacent[Tile](
            up=self.board[adjacent_positions.up],
            right=self.board[adjacent_positions.right],
            down=self.board[adjacent_positions.down],
            left=self.board[adjacent_positions.left]
        )

    def print(self) -> None:
        BoardView("Printing Board", self.board).print()
        
    