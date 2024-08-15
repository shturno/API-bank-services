

class HttpNotFoundError(Exception):
    def __init__(self, message: str = 'Not Found'):
        super().__init__(self.message)
        self.message = message
        self.name = "404 Not Found"
        self.status_code = 404
        