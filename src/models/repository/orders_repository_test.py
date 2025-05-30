from .orders_repository import OrdersRepository

class CollectionMock:
    def __init__(self) -> None:
        self.insert_one_attributes = {}
        self.find_attributes = {}

    def insert_one(self, input_data: any):
        self.insert_one_attributes["dict"] = input_data

    def find(self, *args):
        self.find_attributes["dict"] = args

class DbCollectionMock:
    def __init__(self, collection) -> None:
        self.get_collection_attributes = {}
        self.collection = collection

    def get_collection(self, collection_name):
        self.get_collection_attributes["name"] = collection_name
        return self.collection
    
def test_insert_document():
    collection = CollectionMock()
    db_connection = DbCollectionMock(collection)
    repo = OrdersRepository(db_connection)

    doc = {"alguma": "coisa"}
    repo.insert_document(doc)

    #print()
    #print(collection.insert_one_attributes)
    assert collection.insert_one_attributes["dict"] == doc

def test_select_many_with_properties():
    collection = CollectionMock()
    db_connection = DbCollectionMock(collection)
    repo = OrdersRepository(db_connection)

    doc = {"teste": "find"}
    repo.select_many_with_properties(doc)

    #print()
    #print(collection.find_attributes)
    assert collection.find_attributes["dict"][0] == doc
    assert collection.find_attributes["dict"][1] == {"_id": 0, "cupom": 0}