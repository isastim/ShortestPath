from dataclasses import dataclass, field
import json
from typing import Callable, Dict, List
from app.models.postition import Position
from app.models.tile import Tile
from app.models.board import Board
from app.views.cli.board_view import BoardView
from app.models.field import Field
from app.models.obstacle import Obstacle


@dataclass
class ListBoardAdapter(Board):
    width: int = field(init=False, default=0)
    heigth: int = field(init=False, default=0)
    tiles: Dict[Position, Tile] = field(init=False, default_factory=dict)
    list_board: List
    
    def __post_init__(self) -> None:
        self.__check_list_board_validity()
        self.__list_to_board()
        self.__set_dimensions()
    
    def __check_list_board_validity(self) -> None:
        self.__check_loop([
            self.__check_row_is_not_empty,
            self.__check_row_lengths_match,
        ],[
            self.__check_tile_format
        ])
        
    def __check_row_is_not_empty(self, row: List[str]) -> None:
        if len(row) == 0:
            raise SyntaxError("Rows must not be empty!")
        
    def __check_tile_format(self, tile: str) -> None:
        if tile not in [" ", "X"]:
            raise SyntaxError("Tiles must be declared either ' ' or 'X'!")
    
    def __check_row_lengths_match(self, row) -> None:
        if len(row) != len(self.list_board[0]):
            raise SyntaxError("Rows must be equally long")
    
    def __check_loop(self, row_check_functions: List[Callable], tile_check_functions: List[Callable]) -> None:
        for row in self.list_board:
            for callable in row_check_functions: callable(row)
            for tile in row:
                for callable in tile_check_functions: callable(tile)
    
    def __list_to_board(self) -> None:
        for row_index, row in enumerate(self.list_board):
            for tile_index, tile in enumerate(row):
                self.tiles[Position(tile_index, row_index)] = Field() if tile == " " else Obstacle()

    def __set_dimensions(self) -> None:
        self.width = len(self.list_board[0])
        self.heigth = len(self.list_board)