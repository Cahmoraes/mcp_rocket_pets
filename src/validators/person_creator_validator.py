from typing import Any, cast

from pydantic import BaseModel, Field, ValidationError

from src.errors.error_types import HttpUnprocessableEntityError
from src.views.http_types import HttpRequest


def person_creator_validator(http_request: HttpRequest) -> None:
    class BodyData(BaseModel):
        first_name: str = Field(min_length=1)
        last_name: str = Field(min_length=1)
        age: int | None = None
        pet_id: int

    try:
        BodyData(**cast(dict[str, Any], http_request.body))
    except ValidationError as e:
        raise HttpUnprocessableEntityError(message=e.errors())
