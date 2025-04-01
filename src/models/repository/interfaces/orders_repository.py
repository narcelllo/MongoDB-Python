from abc import ABC, abstractmethod

class OrdersRepositoryInterface(ABC):

    @abstractmethod
    def insert_document(self, document : dict) -> None:
        pass

    @abstractmethod
    def insert_list_of_documentos(self, list_of_documents: list) -> None:
        pass

    @abstractmethod
    def select_many(self, document_filter: dict) -> list:
        pass

    @abstractmethod
    def select_one(self, document_filter: dict) -> dict:
        pass
    
    @abstractmethod
    def select_many_with_properties(self, document_filter: dict) -> list:
        pass

    @abstractmethod
    def select_if_property_exists(self) -> dict:
        pass
    
    @abstractmethod
    def select_by_object_id(self, object_id: str) -> dict:
        pass

    @abstractmethod
    def edit_registry(self, object_id: str, set_cupom: bool) -> dict:
        pass

    @abstractmethod
    def edit_registry_itens(self, object_id: str, set_quantity : int, type_item: str) -> dict:
        pass

    @abstractmethod
    def edit_many_registry(self, set_quantity : str) -> dict:
        pass
    
    @abstractmethod
    def edit_registry_with_increment(self, object_id: str, set_quantity : int) -> dict:
        pass

    @abstractmethod
    def  delete_registry(self, object_id: str) -> None:
        pass

    @abstractmethod
    def  delete_many_registrys(self, object_id: str) -> None:
        pass
