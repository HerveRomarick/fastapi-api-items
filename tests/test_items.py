from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_create_item():
    response = client.post(
        "/items", json={"id": 1, "name": "Laptop", "price": 999.99, "in_stock": True}
    )
    assert response.status_code == 200
    assert response.json()["name"] == "Laptop"


def test_get_items():
    response = client.get("/items")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_update_item():
    response = client.put(
        "/items/1",
        json={"id": 1, "name": "Updated Laptop", "price": 899.99, "in_stock": False},
    )
    assert response.status_code == 200
    assert response.json()["name"] == "Updated Laptop"


def test_delete_item():
    response = client.delete("/items/1")
    assert response.status_code == 200
    assert response.json()["message"] == "Item deleted"
