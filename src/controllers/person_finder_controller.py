from typing import Any

from src.controllers.interfaces.person_finder_controller import (
    PersonFinderControllerInterface,
)
from src.models.sqlite.interfaces.people_repository import PeopleRepositoryInterface


class PersonFinderController(PersonFinderControllerInterface):
    def __init__(self, people_repository: PeopleRepositoryInterface) -> None:
        self.__people_repository = people_repository

    def find(self, person_id: int) -> dict:
        person = self.__find_person_in_db(person_id)
        return self.__format_response(person)

    def __find_person_in_db(self, person_id: int) -> Any:
        person = self.__people_repository.get_person(person_id)
        if not person:
            raise Exception("Pessoa não encontrada")
        return person

    def __format_response(self, person_info: dict) -> dict:
        return {
            "data": {
                "type": "Person",
                "count": 1,
                "attributes": {
                    "first_name": person_info["first_name"],
                    "last_name": person_info["last_name"],
                    "pet_name": person_info["pet_name"],
                    "pet_type": person_info["pet_type"],
                },
            }
        }
