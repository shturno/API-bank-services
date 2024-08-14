from .user_register import UserRegisterController

class MockUserRepository:
    def __init__(self) -> None:
        self.register_user_attributes = {}

    def registry_user(self, username, password) -> None:
        self.register_user_attributes["username"] = username
        self.register_user_attributes["password"] = password

def test_registry():
    repository = MockUserRepository()
    controller = UserRegisterController(repository)
    
    username = "OlaMundo"
    password = "123456"
    
    response = controller.registry(username, password)
    
    assert response["type"] == "User"
    assert response["username"] == username
    
    assert repository.register_user_attributes["username"] == username
    assert repository.register_user_attributes["password"] != None
    assert repository.register_user_attributes["password"] != password