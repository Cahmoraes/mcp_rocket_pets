class HttpUnprocessableEntityError(Exception):
    def __init__(self, **args: object) -> None:
        super().__init__(**args)
        self.status_code = 422
        self.name = "UnprocessableEntity"
        self.message = args["message"]
