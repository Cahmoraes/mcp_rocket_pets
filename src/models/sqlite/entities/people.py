from __future__ import annotations

from typing import TYPE_CHECKING

from sqlalchemy import BIGINT, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.models.sqlite.settings.base import Base

if TYPE_CHECKING:
    from src.models.sqlite.entities import PetsTable


class PeopleTable(Base):
    __tablename__ = "people"

    id: Mapped[int] = mapped_column(BIGINT, primary_key=True)
    first_name: Mapped[str] = mapped_column(String, nullable=False)
    last_name: Mapped[str] = mapped_column(String, nullable=False)
    age: Mapped[int] = mapped_column(BIGINT, nullable=False)
    pet_id: Mapped[int] = mapped_column(ForeignKey("pets.id"))

    pet: Mapped[PetsTable] = relationship()

    def __repr__(self):
        return f"People [name={self.first_name}, lastname={self.last_name}, pet_id={self.pet_id}]"
