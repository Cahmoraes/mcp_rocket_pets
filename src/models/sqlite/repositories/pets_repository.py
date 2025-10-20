from typing import List

from sqlalchemy.exc import UnboundExecutionError

from src.models.sqlite.entities import PetsTable
from src.models.sqlite.interfaces.pets_repository import PetsRepositoryInterface
from src.models.sqlite.settings.connection import DBConnectionHandler


class PetsRepository(PetsRepositoryInterface):
    def __init__(self, db_connection: DBConnectionHandler) -> None:
        self.__db_connection = db_connection

    def list_pets(self) -> List[PetsTable]:
        with self.__db_connection as database:
            try:
                pets = database.session.query(PetsTable).all()
                return pets
            except UnboundExecutionError as exc:
                print(str(exc))
                return []

    def delete_pet(self, name: str) -> None:
        with self.__db_connection as database:
            try:
                (
                    database.session.query(PetsTable)
                    .filter(PetsTable.name == name)
                    .delete()
                )
                database.session.commit()
            except Exception as exception:
                database.session.rollback()
                raise exception
