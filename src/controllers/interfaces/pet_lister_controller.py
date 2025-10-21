from abc import ABC, abstractmethod


class PetListControllerInterface(ABC):
    @abstractmethod
    def list(self) -> dict: ...
