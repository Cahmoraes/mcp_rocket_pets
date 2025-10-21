from typing import List

from src.models.sqlite.entities.pets import PetsTable
from src.models.sqlite.interfaces.pets_repository import PetsRepositoryInterface


class PetListController:
    def __init__(self, pet_repository: PetsRepositoryInterface) -> None:
        self.__pet_repository = pet_repository

    def list(self) -> dict:
        pets = self.__pets_in_db()
        return self.__format_response(pets)

    def __pets_in_db(self) -> List[PetsTable]:
        return self.__pet_repository.list_pets()

    def __format_response(self, pets: List[PetsTable]) -> dict:
        formatted_pets = []
        for pet in pets:
            formatted_pets.append({"id": pet.id, "name": pet.name})
        return {
            "data": {
                "type": "Pets",
                "count": len(formatted_pets),
                "attributes": formatted_pets,
            }
        }
