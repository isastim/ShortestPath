from abc import ABC, abstractmethod


class Interactive(ABC):
    
    @abstractmethod
    def prompt(self) -> None:
        raise NotImplementedError("Not Implemented")