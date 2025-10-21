type Body = dict | None
type Param = dict | None


class HttpResponse:
    def __init__(self, status_code: int, body: Body = None) -> None:
        self.status_code = status_code
        self.body = body
