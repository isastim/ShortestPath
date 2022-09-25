from __future__ import annotations
from copy import copy
from dataclasses import dataclass
from typing import List
from app.models.postition import Position

@dataclass
class Path:
    
    def __init__(self, path: Path=None) -> None:
        if path is None:
            self.positions: List[Position] = []
        else:
            self.positions: List[Position] = list(path.positions)
        
    
    def __add__(self, position: Position) -> None:
        self.positions.append(position)
    
    def __copy__(self) -> Path:
        return Path(self)
    
    def __len__(self) -> int:
        return self.positions.__len__()
    
    def __lt__(self, other: Path) -> bool:
        self.__len__() < other.__len__()
    
    def __gt__(self, other: Path) -> bool:
        self.__len__() > other.__len__()
    
    def __eq__(self, other: Path) -> bool:
        self.positions == other.positions
    
a = Path()
b = copy(a)
print()