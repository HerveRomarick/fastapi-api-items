from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_item():
    response = client.post("/items", json={
        "id": 1,
        "name": "Test Item",
        "price": 10.0,
        "in_stock": True
    })
    assert response.status_code == 200
    assert response.json()["name"] == "Test Item"
    assert response.json()["price"] == 10.0
    assert response.json()["in_stock"] is True