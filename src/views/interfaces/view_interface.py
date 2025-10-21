from abc import ABC, abstractmethod

from src.views.http_types import HttpRequest, HttpResponse


class ViewInterface(ABC):
    @abstractmethod
    def handle(self, http_request: HttpRequest) -> HttpResponse: ...
