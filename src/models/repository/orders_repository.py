from bson.objectid import ObjectId

class OrdersRepository:
    def __init__(self, db_connection) -> None:
        self.__collection_name = "orders"
        self.__db_connection = db_connection

    def insert_document(self, document : dict) -> None:
        collection = self.__db_connection.get_collection(self.__collection_name)
        collection.insert_one(document)

    def insert_list_of_documentos(self, list_of_documents: list) -> None:
        collection = self.__db_connection.get_collection(self.__collection_name)
        collection.insert_many(list_of_documents)

    def select_many(self, document_filter: dict) -> list:
        collection = self.__db_connection.get_collection(self.__collection_name)
        data = collection.find(
            document_filter
        )
        return data
    
    def select_one(self, document_filter: dict) -> dict:
        collection = self.__db_connection.get_collection(self.__collection_name)
        response = collection.find_one(document_filter)
        return response
    
    def select_many_with_properties(self, document_filter: dict) -> list:
        collection = self.__db_connection.get_collection(self.__collection_name)
        data = collection.find(
            document_filter, 
            {"_id": 0, "cupom": 0} #opção de retorno 
        )
        return data
    
    def select_if_property_exists(self) -> dict:
        collection = self.__db_connection.get_collection(self.__collection_name)
        response = collection.find({"addres": {"$exists": True}},
                                    {"_id": 0, "cupom": 0})
        return response
    
    def select_by_object_id(self, object_id: str) -> dict: 
        collection = self.__db_connection.get_collection(self.__collection_name)
        data = collection.find_one({"_id": ObjectId(object_id)})
        return data
    
    def edit_registry(self, object_id: str, set_cupom: bool) -> dict:
        collection = self.__db_connection.get_collection(self.__collection_name)
        collection.update_one(
            {"_id": ObjectId(object_id)},
            {"$set": {"cupom": set_cupom}}
        )

    def edit_registry_itens(self, object_id: str, set_quantity : int, type_item: str) -> dict:
        collection = self.__db_connection.get_collection(self.__collection_name)
        collection.update_one(
            {"_id": ObjectId(object_id)},
            {"$set": {"itens.pizza.quantidade": set_quantity ,"itens.pizza.tipo": type_item}}
        )

    def edit_many_registry(self, set_quantity : str) -> dict:
        collection = self.__db_connection.get_collection(self.__collection_name)
        collection.update_many(
            {"itens.refrigerante": {"$exists": True}},
            {"$set": {"itens.refrigerante.quantidade": set_quantity }}
        )


    def edit_registry_with_increment(self, object_id: str, set_quantity : int) -> dict:
        collection = self.__db_connection.get_collection(self.__collection_name)
        collection.update_one(
            {"_id": ObjectId(object_id)},
            {"$inc": {"itens.pizza.quantidade": set_quantity }}
        )

    def  delete_registry(self, object_id: str) -> None:
        collection = self.__db_connection.get_collection(self.__collection_name)
        collection.delete_one({"_id": ObjectId(object_id)})

    def  delete_many_registrys(self, object_id: str) -> None:
        collection = self.__db_connection.get_collection(self.__collection_name)
        collection.delete_many(
            {"itens.refrigerante": {"$exists": True}},
        )