from abc import ABC, abstractmethod
from typing import Any


class PeopleRepositoryInterface(ABC):
    @abstractmethod
    def insert_person(
        self, first_name: str, last_name: str, age: int, pet_id: int
    ) -> None: ...

    @abstractmethod
    def get_person(self, person_id: int) -> Any: ...
