from dataclasses import dataclass, field
from app.models.tile import Tile

@dataclass
class Field(Tile):
    value: str = field(default=" ", init=False)
