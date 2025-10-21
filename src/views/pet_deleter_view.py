from src.controllers.interfaces import PetDeleterControllerInterface
from src.views.http_types import HttpRequest, HttpResponse
from src.views.interfaces.view_interface import ViewInterface


class PetDeleterView(ViewInterface):
    def __init__(self, controller: PetDeleterControllerInterface) -> None:
        self.__controller = controller

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        if not http_request.param:
            raise Exception("Parâmetro inválido")
        name = http_request.param["name"]
        body_response = self.__controller.delete(name)
        return HttpResponse(status_code=204, body=body_response)
