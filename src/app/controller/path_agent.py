from dataclasses import dataclass, field
from typing import List
from app.models.tile import Tile
from app.models.obstacle import Obstacle
from app.models.adjacent import Adjacent
from app.models.board import Board
from app.models.postition import Position
from app.models.position_factory import PositionFactory
from app.views.cli.position_view import PositionView

@dataclass
class PathAgent:
    board: Board
    shortest_path: List[Position] = field(init=False, default_factory=list)
        
    def find_shortest_path(self, start_position: Position, destination_position: Position, current_path: List[Position]=[]) -> List[Position]:
        current_path = current_path + [start_position]
        adjacent_positions: Adjacent[Position] = PositionFactory.get_adjacent_positions(start_position, self.board)
        if destination_position in adjacent_positions:
            return current_path
        paths: List[List[Position]] = [
            self.find_shortest_path(position, destination_position, current_path)
            for position in adjacent_positions 
            if self.__should_check_position(position, current_path)
        ]
        self.shortest_path = self.__get_smallest_list(paths) or self.shortest_path
        return self.shortest_path
        
    def __get_smallest_list(self, lists: List[List]) -> List:
        if len(lists) is 0:
            return None
        smallest_list = lists[0]
        for list_entry in lists:
            smallest_list = list_entry if list_entry.__len__() < smallest_list.__len__() else smallest_list
        return smallest_list
    
    def __is_obstacle(self, tile: Tile) -> bool:
        return isinstance(tile, Obstacle)
    
    def __is_position_passable(self, position: Position) -> bool:
        if position is None:
            return False
        if self.__is_obstacle(self.board[position]):
            return False
        return True
    
    def __is_position_already_in_path(self, position: Position, current_path: List[Position]) -> bool:
        return position in current_path
    
    def __should_check_position(self, position: Position, current_path: List[Position]) -> bool:
        return self.__is_position_passable(position) and not self.__is_position_already_in_path(position, current_path)
    
    def print(self) -> None:
        PositionView("Printing Shortest Path", self.board, self.shortest_path).print()