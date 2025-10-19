from typing import cast
from unittest import mock

import pytest
from mock_alchemy.mocking import UnifiedAlchemyMagicMock

from src.models.sqlite.entities import PetsTable
from src.models.sqlite.settings.connection import DBConnectionHandler

from . import PetsRepository


class MockConnection(DBConnectionHandler):
    def __init__(self) -> None:
        super().__init__()
        self.session = UnifiedAlchemyMagicMock(
            data=[
                (
                    [mock.call.query(PetsTable)],
                    [
                        PetsTable(name="dog", type="dog"),
                        PetsTable(name="cat", type="cat"),
                    ],
                )
            ]
        )

    @property
    def session_mock(self) -> UnifiedAlchemyMagicMock:
        if not isinstance(self.session, UnifiedAlchemyMagicMock):
            raise Exception("Session is not UnifiedAlchemyMagicMock")
        return self.session

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, exc_tb): ...


class MockConnectionNoResult(DBConnectionHandler):
    def __init__(self) -> None:
        super().__init__()
        self.session = UnifiedAlchemyMagicMock()
        self.session.query.side_effect = self.__raise_no_result_found

    def __raise_no_result_found(self, *args, **kwargs) -> None:
        raise Exception("No result found")

    @property
    def session_mock(self) -> UnifiedAlchemyMagicMock:
        if not isinstance(self.session, UnifiedAlchemyMagicMock):
            raise Exception("Session is not UnifiedAlchemyMagicMock")
        return self.session

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, exc_tb): ...


def test_list_pets():
    mock_connection = MockConnection()
    repo = PetsRepository(mock_connection)
    response = repo.list_pets()
    mock_connection.session_mock.query.assert_called_once_with(PetsTable)
    mock_connection.session_mock.all.assert_called_once()
    mock_connection.session_mock.filter.assert_not_called()
    assert response[0].name == "dog"


def test_delete_pet():
    pet_name = "pet_name"
    mock_connection = MockConnection()
    repo = PetsRepository(mock_connection)
    repo.delete_pet(pet_name)
    mock_connection.session_mock.query.assert_called_once_with(PetsTable)
    mock_connection.session_mock.filter.assert_called_once_with(
        PetsTable.name == pet_name
    )
    mock_connection.session_mock.delete.assert_called_once()


def test_list_pets_no_results():
    mock_connection = MockConnectionNoResult()
    repo = PetsRepository(mock_connection)
    with pytest.raises(Exception) as exc:
        response = repo.list_pets()
        assert response == []
    assert str(exc.value) == "No result found"


def test_delete_pet_error():
    pet_name = "pet_name"
    mock_connection = cast(UnifiedAlchemyMagicMock, MockConnectionNoResult())
    repo = PetsRepository(mock_connection)
    with pytest.raises(Exception) as exc:
        repo.delete_pet(pet_name)
    assert str(exc.value) == "No result found"
    mock_connection.session.rollback.assert_called_once()
