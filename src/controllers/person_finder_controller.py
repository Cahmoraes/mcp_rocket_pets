from typing import Any

from src.controllers.interfaces.person_finder_controller import (
    PersonFinderControllerInterface,
)
from src.errors.error_types import HttpNotFoundError
from src.models.sqlite.interfaces import PeopleRepositoryInterface


class PersonFinderController(PersonFinderControllerInterface):
    def __init__(self, people_repository: PeopleRepositoryInterface) -> None:
        self.__people_repository = people_repository

    def find(self, person_id: int) -> dict:
        person = self.__find_person_in_db(person_id)
        return self.__format_response(person)

    def __find_person_in_db(self, person_id: int) -> Any:
        person = self.__people_repository.get_person(person_id)
        if not person:
            raise HttpNotFoundError("Pessoa não encontrada")
        return person

    def __format_response(self, person_info: Any) -> dict:
        return {
            "data": {
                "type": "Person",
                "count": 1,
                "attributes": {
                    "first_name": person_info[0],
                    "last_name": person_info[1],
                    "pet_name": person_info[2],
                    "pet_type": person_info[3],
                },
            }
        }
