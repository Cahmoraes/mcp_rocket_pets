from typing import Any

import pytest

from src.models.sqlite.interfaces.people_repository import PeopleRepositoryInterface

from .person_creator_controller import PersonCreatorController


class MockPeopleRepository(PeopleRepositoryInterface):
    def insert_person(
        self, first_name: str, last_name: str, age: int, pet_id: int
    ) -> None:
        pass

    def get_person(self, person_id: int) -> Any:
        return None


def test_create():
    person_info = {
        "first_name": "Fulano",
        "last_name": "de Tal",
        "age": 30,
        "pet_id": 123,
    }
    controller = PersonCreatorController(MockPeopleRepository())
    response = controller.create(person_info)
    assert response["data"]["type"] == "Person"
    assert response["data"]["count"] == 1
    assert response["data"]["attributes"] == person_info


def test_create_error():
    person_info = {
        "first_name": "Fulano123",
        "last_name": "de Tal",
        "age": 30,
        "pet_id": 123,
    }

    controller = PersonCreatorController(MockPeopleRepository())
    with pytest.raises(Exception) as exc:
        controller.create(person_info)
    assert str(exc.value) == "Nome da pessoa inválido"
