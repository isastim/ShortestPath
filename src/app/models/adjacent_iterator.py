from __future__ import annotations
from typing import Dict, Generic, TypeVar, TYPE_CHECKING
if TYPE_CHECKING:
    from app.models.adjacent import Adjacent



T = TypeVar("T")


class AdjacentIterator(Generic[T]):
    def __init__(self, adjacent: Adjacent[T]) -> None:
        self.adjacent = adjacent
        self.index = 0
        self.index_mapping: Dict[int, T] = {
            0: self.adjacent.up,
            1: self.adjacent.right,
            2: self.adjacent.down,
            3: self.adjacent.left,
        }

    def __next__(self) -> Adjacent[T]:
        try:
            result: Adjacent[T] = self.index_mapping[self.index]
            self.index += 1
            return result
        except KeyError:
            raise StopIteration