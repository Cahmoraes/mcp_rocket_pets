from sqlalchemy import Engine, create_engine
from sqlalchemy.orm import Session, sessionmaker

from src.models.sqlite.settings.base import Base

from . import ConnectionHandlerInterface


class DBConnectionHandler(ConnectionHandlerInterface):
    def __init__(self) -> None:
        self.__connection_string = "sqlite:///storage.db"
        self.__engine = None
        self.__session = None

    def connect_to_db(self):
        self.__engine = create_engine(self.__connection_string)

    @property
    def engine(self) -> Engine | None:
        return self.__engine

    @property
    def session(self) -> Session:
        if not self.__session:
            raise Exception("Session not defined")
        return self.__session

    @session.setter
    def session(self, session: Session) -> None:
        self.__session = session

    def recreate_db(self) -> None:
        Base.metadata.drop_all(self.__engine)
        Base.metadata.create_all(self.__engine)

    def __enter__(self):
        session_maker = sessionmaker()
        self.__session = session_maker(bind=self.engine)
        return self

    def __exit__(self, exc_type, exc_value, exc_tb):
        if self.__session is None:
            return

        self.__session.close()


db_connection_handler = DBConnectionHandler()
