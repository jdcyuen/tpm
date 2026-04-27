from abc import ABC, abstractmethod
from typing import List
from src.models.position import Position


class BaseProvider(ABC):
    @abstractmethod
    def get_positions(self) -> List[Position]:
        pass
