

class HttpUnauthorizedError(Exception):
    def __init__(self, message: str = 'Not Found'):
        super().__init__(self.message)
        self.message = message
        self.name = "401 Unauthorized"
        self.status_code = 401
        