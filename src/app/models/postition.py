from dataclasses import dataclass, field




@dataclass(frozen=True)
class Position:
    x: int
    y: int    

    def __lt__(self, other: object):
        return self.y < other.y

    def __gt__(self, other: object):
        return self.y > other.y
    
    def __eq__(self, other: object) -> bool:
        if other is None:
            return False
        return self.x == other.x and self.y == other.y

# class Position:
#     def __init__(self, x: int, y: int) -> None:
#         self.x = x
#         self.y = y

#     def __str__(self) -> str:
#         return f"[{self.x}, {self.y}]"

#     def __lt__(self, other: object):
#         return self.y < other.y

#     def __gt__(self, other: object):
#         return self.y > other.y
    
#     def __eq__(self, other: object) -> bool:
#         if other is None:
#             return False
#         return self.x == other.x and self.y == other.y
    
#     def __hash__(self) -> int:
#         return hash((self.x, self.y))