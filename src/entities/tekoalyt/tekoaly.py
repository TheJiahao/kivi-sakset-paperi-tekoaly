from abc import ABC, abstractmethod


class Tekoaly(ABC):
    def __init__(self) -> None:
        pass

    @abstractmethod
    def pelaa(self, syote: str) -> str:
        pass
