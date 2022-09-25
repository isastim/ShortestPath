from dataclasses import dataclass
from typing import Generic, TypeVar
from app.models.adjacent_iterator import AdjacentIterator

from app.models.postition import Position

T = TypeVar("T")

class Adjacent(Generic[T]):
    def __init__(self, up: T, right: T, down: T, left: T) -> None:
        self.up = up
        self.right = right
        self.down = down
        self.left = left
        
    def __contains__(self,other: T):
        return other in [self.up, self.right, self.down, self.left]
    
    def __iter__(self) -> AdjacentIterator[T]:
        return AdjacentIterator[T](self)