from __future__ import annotations

from typing import TYPE_CHECKING

from sqlalchemy import BIGINT, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.models.sqlite.settings.base import Base

if TYPE_CHECKING:
    from src.models.sqlite.entities.people import PeopleTable


class PetsTable(Base):
    __tablename__ = "pets"

    id: Mapped[int] = mapped_column(BIGINT, primary_key=True)
    name: Mapped[str] = mapped_column(String, nullable=False, unique=True)
    type: Mapped[str] = mapped_column(String, nullable=False, unique=True)

    owner: Mapped[PeopleTable] = relationship(back_populates="pets")

    def __repr__(self):
        return f"Pets [name={self.name}], type={self.type}"
