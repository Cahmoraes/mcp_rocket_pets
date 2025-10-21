from src.controllers.interfaces import PersonCreatorControllerInterface
from src.views.http_types import HttpRequest, HttpResponse
from src.views.interfaces.view_interface import ViewInterface


class PersonCreatorView(ViewInterface):
    def __init__(self, controller: PersonCreatorControllerInterface) -> None:
        self.__controller = controller

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        person_info = http_request.body
        if not person_info:
            raise Exception("Body inválido")
        body_response = self.__controller.create(person_info)
        return HttpResponse(status_code=201, body=body_response)
