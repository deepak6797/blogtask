from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float

# In-memory database for items
test_db = {}

def get_item_by_id(item_id: int):
    if item_id in test_db:
        return test_db[item_id]
    else:
        raise ValueError("Item not found")

@app.post("/items/")
async def create_item(item: Item):
    if item.price < 0:
        raise ValueError("Price cannot be negative")
    item_id = len(test_db) + 1  # Simple ID generation
    test_db[item_id] = item
    return {"id": item_id, "name": item.name, "price": item.price}

@app.get("/items/{item_id}")
async def read_item(item_id: int):
    item = get_item_by_id(item_id)
    return item
