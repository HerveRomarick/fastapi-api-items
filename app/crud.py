from app.models import items_db
from app.schemas import Item


def list_items():
    return list(items_db.values())


def get_item(item_id: int):
    return items_db.get(item_id)


def create_item(item: Item):
    if item.id in items_db:
        raise ValueError("Item already exists")
    items_db[item.id] = item
    return item


def update_item(item_id: int, item: Item):
    if item_id not in items_db:
        raise ValueError("Item not found")
    items_db[item_id] = item
    return item


def delete_item(item_id: int):
    return items_db.pop(item_id, None)
