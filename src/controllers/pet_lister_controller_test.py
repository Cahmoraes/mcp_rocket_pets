from src.models.sqlite.entities.pets import PetsTable
from src.models.sqlite.interfaces.pets_repository import PetsRepositoryInterface

from .pet_lister_controller import PetListController


class MockPetsRepository(PetsRepositoryInterface):
    def list_pets(self) -> list[PetsTable]:
        return [
            PetsTable(name="Fluffy", type="Cat", id=4),
            PetsTable(name="Buddy", type="Dog", id=47),
        ]

    def delete_pet(self, name: str) -> None: ...


def test_list_pets():
    controller = PetListController(MockPetsRepository())
    response = controller.list()
    expected_response = {
        "data": {
            "type": "Pets",
            "count": 2,
            "attributes": [{"name": "Fluffy", "id": 4}, {"name": "Buddy", "id": 47}],
        }
    }
    assert response == expected_response
