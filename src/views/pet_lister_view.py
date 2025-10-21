from src.controllers.interfaces import PetListerControllerInterface
from src.views.http_types import HttpRequest, HttpResponse
from src.views.interfaces.view_interface import ViewInterface


class PetListerView(ViewInterface):
    def __init__(self, controller: PetListerControllerInterface) -> None:
        self.__controller = controller

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        body_response = self.__controller.list()
        return HttpResponse(status_code=201, body=body_response)
