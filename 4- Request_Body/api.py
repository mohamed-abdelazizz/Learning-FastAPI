from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()


# ---------------------------
# Root Endpoint
# ---------------------------
@app.get("/")
async def read_root():
    # Returns a simple greeting message
    return {"message": "Hello, World!"}


# ---------------------------
# In-Memory Items Database
# ---------------------------
items = [
    {"id": 1, "name": "book", "price": "15", "stock": True},
    {"id": 2, "name": "game", "price": "50", "stock": True},
    {"id": 3, "name": "cd", "price": "30", "stock": True},
    {"id": 4, "name": "magazine", "price": "10", "stock": False},
    {"id": 5, "name": "book", "price": "10", "stock": True},
    {"id": 6, "name": "games", "price": "10", "stock": True},
]


# ---------------------------
# Pydantic Model for Items
# ---------------------------
# - Uses Pydantic BaseModel to validate request body.
class Item(BaseModel):
    name: str
    description: Optional[str] = None  # description: str | None = None
    price: float
    tax: Optional[float] = None


# ---------------------------
# Create Item (POST)
# ---------------------------
@app.post("/items")
async def create_item(item: Item):
    # Convert Pydantic model -> Python dict
    item_dict = item.dict()

    # Include total price only if tax is provided
    if item.tax:
        total_price = item.price + (item.price * item.tax)
        item_dict.update({"total_price": total_price})

    return item_dict


# ---------------------------
# Update Item (PUT)
# ---------------------------
@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    # Combine item_id with all item fields (dict unpacking)
    # ** => unpacks the dict into key-value pairs
    updated_item = {"item_id": item_id, **item.dict()}
    return updated_item


# ---------------------------------------------------------
# EXPLANATION: Why We Use Pydantic BaseModel in FastAPI?
# ---------------------------------------------------------
"""
Pydantic BaseModel is the heart of FastAPI’s data validation.

Why use BaseModel?

1) Automatic Validation:
   - Ensures fields have correct types (str, float, email, etc.)
   - Returns clear error messages if data is invalid.

2) Automatic Type Conversion:
   - If price comes as a string "20.5", Pydantic converts it to float automatically.

3) Cleaner, Safer Code:
   - Instead of using dictionaries like body["item"]["name"],
     you can directly use item.name which is safer and easier.

4) Automatic JSON Serialization:
   - Returning BaseModel objects → FastAPI converts to JSON automatically.

5) Swagger Documentation:
   - BaseModels appear in the interactive docs automatically with full schemas.

6) Structured Data:
   - Useful for complex nested data and large APIs.

Example:
--------
class Item(BaseModel):
    name: str
    description: str
    price: float

This ensures every request contains:
- name (string)
- description (string)
- price (float)

If the client sends wrong data, FastAPI returns a clear validation error.

In summary, using Pydantic
BaseModel = clean code + safety + validation + auto docs + easy JSON handling.
"""
