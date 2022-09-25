from abc import ABC, abstractmethod
from dataclasses import dataclass

@dataclass
class View(ABC):
    title: str
    
    @abstractmethod    
    def print(self) -> None:
        raise NotImplementedError("Not Implemented")