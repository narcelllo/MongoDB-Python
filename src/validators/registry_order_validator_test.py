import pytest
from .registry_order_validator import registry_order_validator

def test_registry_order_validator():
    body = {
        "data": {
            "name": "joaozinho",
            "address": "rua do limao",
            "cupom": False,
            "items": [
                {"item": "Refrigerante", "quantity": 2},
                {"item": "pizza", "quantity": 3}
            ]
        }
    }
    registry_order_validator(body)

def test_registry_order_validator_errors():
    body_with_error = {
        "data": {
            "name": "joaozinho",
            "address": "rua do limao",
            "cupom": "False",
            "items": [
                {"item": "Refrigerante", "quantity": 2},
                {"item": "pizza", "quantity": 3}
            ]
        }
    }
    with pytest.raises(Exception):
        registry_order_validator(body_with_error)