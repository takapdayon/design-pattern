from abc import ABC, abstractmethod
from Iterator import Iterator

class Aggregate(ABC):
    @abstractmethod
    def iterator(self) -> Iterator:
        pass
