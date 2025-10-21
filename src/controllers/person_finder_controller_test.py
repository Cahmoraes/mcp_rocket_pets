from typing import Any, TypedDict

from src.models.sqlite.interfaces.people_repository import PeopleRepositoryInterface

from .person_finder_controller import PersonFinderController


class MockPerson(TypedDict):
    first_name: str
    last_name: str
    pet_name: str
    pet_type: str


class MockRepository(PeopleRepositoryInterface):
    def get_person(self, person_id: int) -> Any:
        return MockPerson(
            first_name="John", last_name="Doe", pet_name="Fluffy", pet_type="cat"
        )

    def insert_person(
        self, first_name: str, last_name: str, age: int, pet_id: int
    ) -> None:
        return


def test_find():
    controller = PersonFinderController(MockRepository())
    response = controller.find(person_id=123)
    expected_response = {
        "data": {
            "type": "Person",
            "count": 1,
            "attributes": {
                "first_name": "John",
                "last_name": "Doe",
                "pet_name": "Fluffy",
                "pet_type": "cat",
            },
        }
    }
    assert response == expected_response
