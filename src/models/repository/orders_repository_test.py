import pytest
from src.models.connection.connection_handler import DBConnectionhandler
from .orders_repository import OrdersRepository

db_connection_handler = DBConnectionhandler()
db_connection_handler.connect_to_db()
conn = db_connection_handler.get_db_connection()

@pytest.mark.skip(reason="Integration test")
def test_insert_document():
    orders_repository = OrdersRepository(conn)
    my_doc = {"doc": "test", "valor": 0}
    orders_repository.insert_document(my_doc)

@pytest.mark.skip(reason="Integration test")
def test_insert_list_document():
    orders_repository = OrdersRepository(conn)
    my_doc = [{"doc1": "test", "valor": 0}, {"doc2": "test", "valor": 1}, {"doc3": "test", "valor": 2}]
    orders_repository.insert_list_of_documentos(my_doc)

@pytest.mark.skip(reason="list test documents")
def test_select_many():
    orders_repository = OrdersRepository(conn)
    doc_filter = {"cupom": True}
    response = orders_repository.select_many(doc_filter)
    print()
    print(response)

    for doc in response:
        print(doc)
        print()
        print(doc["itens"])
        print()
        
@pytest.mark.skip(reason="list test documents")
def test_select_one():
    orders_repository = OrdersRepository(conn)
    doc_filter = {"cupom": False}
    response = orders_repository.select_one(doc_filter)
    print()
    print(response)

@pytest.mark.skip(reason="list test documents")
def test_select_many_with_properties():
    orders_repository = OrdersRepository(conn)
    doc_filter = {"cupom": True}
    response = orders_repository.select_many_with_properties(doc_filter)
    print()
    print(response)

    for doc in response:
        print(doc)
        print()
        print(doc["itens"])
        print()

@pytest.mark.skip(reason="list test documents")
def test_select_if_property_exists():
    orders_repository = OrdersRepository(conn)
    response = orders_repository.select_if_property_exists()
    for doc in response:
        print(doc)
        print()

@pytest.mark.skip(reason="list test documents")
def test_select_many_with_and_filter():
    orders_repository = OrdersRepository(conn)
    doc_filter = {
        "cupom": True,
        "itens.doce": {"$exists": True}
    } #Busca AND
    response = orders_repository.select_many(doc_filter)
    print()
    print(response)

    for doc in response:
        print(doc)
        print()

@pytest.mark.skip(reason="list test documents")
def test_select_many_with_or_filter():
    orders_repository = OrdersRepository(conn)
    doc_filter = {
        "$or":[
            {"addres": {"$exists": True}},
            {"itens.doce.tipo": "chocolate"}
               ]
    } #Busca OR
    response = orders_repository.select_many(doc_filter)
    print()

    for doc in response:
        print(doc)
        print()

@pytest.mark.skip(reason="list test documents")
def test_elect_by_object_id():
    orders_repository = OrdersRepository(conn)
    object_id = "67e8492e8eeedae82a4abea1"
    response = orders_repository.select_by_object_id(object_id)
    print(response)
