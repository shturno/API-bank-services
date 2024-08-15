from src.controllers.interfaces.balance_editor import BalanceEditorInterface
from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse
from .interfaces.view_interface import ViewInterface

class BalanceEditorView:
    def __init__(self, controller: BalanceEditorInterface) -> None:
        self.__controller = controller
        
    def handle(self, http_request: HttpRequest)-> HttpResponse:
        new_balance = http_request.body.get("new_balance")
        user_id = http_request.params.get("user_id")
        self.__validate_inputs(new_balance, user_id)
        
        response = self.__controller.edit(user_id, new_balance)
        
    def __validate_inputs(self, new_balance: any, user_id: any) -> None:
        if not new_balance or not user_id or not isinstance(new_balance, int) or not isinstance(user_id, int):
            raise Exception("Invalid inputs")
        
        if new_balance < 0:
            raise Exception("Invalid inputs")
        
        if user_id < 0:
            raise Exception("Invalid inputs")
        
        return None