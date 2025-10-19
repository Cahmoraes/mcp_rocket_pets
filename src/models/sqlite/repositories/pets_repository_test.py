from unittest import mock

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


def test_list_pets():
    mock_connection = MockConnection()
    repo = PetsRepository(mock_connection)
    response = repo.list_pets()
    mock_connection.session_mock.query.assert_called_once_with(PetsTable)
    mock_connection.session_mock.all.assert_called_once()
    mock_connection.session_mock.filter.assert_not_called()
    assert response[0].name == "dog"
