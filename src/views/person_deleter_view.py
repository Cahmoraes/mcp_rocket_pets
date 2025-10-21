from src.controllers.interfaces import PetDeleterControllerInterface
from src.views.http_types import HttpRequest, HttpResponse
from src.views.interfaces.view_interface import ViewInterface


class PersonDeleterView(ViewInterface):
    def __init__(self, controller: PetDeleterControllerInterface) -> None:
        self.__controller = controller

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        if not http_request.body:
            raise Exception("Body inválido")
        pet_name = http_request.body["name"]
        self.__controller.delete(pet_name)
        return HttpResponse(status_code=204)
