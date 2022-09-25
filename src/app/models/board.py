from dataclasses import dataclass, field
from typing import Dict
from app.models.field import Field
from app.models.obstacle import Obstacle
from app.models.postition import Position
from app.models.tile import Tile

@dataclass
class Board:
    width: int
    heigth: int
    tiles: Dict[Position, Tile] = field(init=False, default_factory=dict)
    
    def __post_init__(self) -> None:
        self.tiles = {Position(y,x): Field() for x in range(self.width) for y in range(self.heigth)}
        self.tiles = dict(sorted(self.tiles.items()))
        
    # def __init__(self, width: int, height: int) -> None:
    #     self.width: int = width
    #     self.heigth: int = height
    #     self.tiles: Dict[Position, Tile] = {Position(y,x): Field() for x in range(width) for y in range(height)}
    #     self.tiles = dict(sorted(self.tiles.items()))


    def __str__(self) -> str:
        buffer: str = ""
        for tile in self.tiles.values():
            buffer = f"{buffer}[{tile}]"
        return buffer

    def __getitem__(self, position: Position) -> Tile:
        if position is None:
            return None
        return self.tiles[position]
    
    def __setitem__(self, position: Position, tile: Tile) -> None:
        self.tiles[position] = tile
        