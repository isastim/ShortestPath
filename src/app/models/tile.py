from abc import ABC
from dataclasses import dataclass, field


@dataclass
class Tile(ABC):
    value: str = field(init=False)

    def __str__(self) -> str:
        return f"[{self.value}]"
        