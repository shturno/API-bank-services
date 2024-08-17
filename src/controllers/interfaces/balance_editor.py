from abc import ABC, abstractmethod

class BalanceEditorInterface(ABC):
    
    @abstractmethod
    def edit(self, user_id: int, username:str, balance:float) -> dict: pass