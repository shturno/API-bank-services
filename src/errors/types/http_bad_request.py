

class HttpBadRequestError(Exception):
    def __init__(self, message: str) -> None:
        super().__init__(self.message)
        self.message = message
        self.name = "400 Bad Request"
        self.status_code = 400
        
        