from fastapi import FastAPI
from app import schemas

app = FastAPI()
items_db = []


@app.get("/items")
def list_items1():
    return items_db


@app.get("/items")
def list_items() -> list:
    return items_db


@app.get("/")
def read_root():
    return {"message": "API FastAPI fonctionne !"}


@app.get("/items/{item_id}")
def get_item(item_id: int):
    for item in items_db:
        if item["id"] == item_id:
            return item
    return {"error": "Item not found"}


@app.post("/items")
def create_item(item: schemas.Item):
    items_db.append(item.dict())
    return item


@app.put("/items/{item_id}")
def update_item(item_id: int, new_item: schemas.Item):
    for i, item in enumerate(items_db):
        if item["id"] == item_id:
            items_db[i] = new_item.dict()
            return new_item
    return {"error": "Item not found"}


@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    for item in items_db:
        if item["id"] == item_id:
            items_db.remove(item)
            return {"message": "Item deleted"}
    return {"error": "Item not found"}
