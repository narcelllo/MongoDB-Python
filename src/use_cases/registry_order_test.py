from src.main.http_types.http_request import HttpRequest
from src.use_cases.registry_order import RegistryOrder

class OrdersRepositoryMock: 
    def __init__(self) -> None: 
        self.insert_document_att = {} 
    def insert_document(self, document: dict) -> None: 
        self.insert_document_att ["document"] = document

class OrdersRepositoryMockError: 
    def insert_document(self, document: dict) -> None: 
        raise Exception("erro aqui") 

    def test_registry(): 
        repo = OrdersRepositoryMock() 
        registry_order = RegistryOrder(repo)

        mock_registry = HttpRequest(
            body={
                "data": { 
                "name": "joaozinho", 
                "address": "rua do limao", 
                "cupom": False, 
                "items": [ 
                    {"item": "Refrigerante", "quantidade": 2}, 
                    { "item": "pizza", "quantidade": 3} 
                ]
            } 
        } 
    ) 
        response = registry_order.registry(mock_registry)
        print()
        print(response)