from dataclasses import dataclass, field
from app.models.tile import Tile

@dataclass
class Obstacle(Tile):
    value: str = field(default="X", init=False)
    