from src.views.http_types.http_request import HttpRequest

from .person_creator_validator import person_creator_validator

type Body = dict | None


class MockRequest(HttpRequest):
    def __init__(self, body: dict | None = None, param: dict | None = None) -> None:
        super().__init__(body, param)


def test_person_creator_validator():
    request = MockRequest(
        {"first_name": "fulano", "last_name": "deTal", "age": 3, "pet_id": 7}
    )
    person_creator_validator(request)
