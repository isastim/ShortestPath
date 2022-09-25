from app.models.adjacent import Adjacent
from app.models.board import Board
from app.models.postition import Position


class PositionFactory:

    @staticmethod
    def __check_boundaries(position: Position, board: Board) -> Position:
        if min(position.x, position.y) < 0:
            return None
        if position.x >= board.width or position.y >= board.heigth:
            return None
        return position

    @staticmethod
    def get_left_adjacent_position(position: Position, board: Board) -> Position:
        left_position: Position = Position(position.x-1, position.y)
        return PositionFactory.__check_boundaries(left_position, board)

    @staticmethod
    def get_right_adjacent_position(position: Position, board: Board) -> Position:
        right_position: Position = Position(position.x+1, position.y)
        return PositionFactory.__check_boundaries(right_position, board)

    @staticmethod
    def get_up_adjacent_position(position: Position, board: Board) -> Position:
        up_position: Position = Position(position.x, position.y-1)
        return PositionFactory.__check_boundaries(up_position, board)

    @staticmethod
    def get_down_adjacent_position(position: Position, board: Board) -> Position:
        down_position: Position = Position(position.x, position.y+1)
        return PositionFactory.__check_boundaries(down_position, board)
    
    @staticmethod
    def get_adjacent_positions(position: Position, board: Board) -> Adjacent[Position]:
        return Adjacent[Position](
            up=PositionFactory.get_up_adjacent_position(position, board),
            right=PositionFactory.get_right_adjacent_position(position, board),
            down=PositionFactory.get_down_adjacent_position(position, board),
            left=PositionFactory.get_left_adjacent_position(position, board)
        )