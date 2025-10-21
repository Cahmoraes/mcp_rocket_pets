type Body = dict | None
type Param = dict | None


class HttpRequest:
    def __init__(self, body: Body = None, param: Param = None) -> None:
        self.body = body
        self.param = param
