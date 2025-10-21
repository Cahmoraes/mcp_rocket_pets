from src.controllers.interfaces import PersonFinderControllerInterface
from src.views.http_types import HttpRequest, HttpResponse
from src.views.interfaces.view_interface import ViewInterface


class PersonFinderView(ViewInterface):
    def __init__(self, controller: PersonFinderControllerInterface) -> None:
        self.__controller = controller

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        person_id = http_request.body
        if not person_id or not isinstance(person_id, int):
            raise Exception("Body inválido")
        body_response = self.__controller.find(person_id)
        return HttpResponse(status_code=200, body=body_response)
