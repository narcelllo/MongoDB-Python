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