from fastapi import FastAPI, Path, Query, Body
from pydantic import BaseModel

app = FastAPI()


# -----------------------------------
# Root Endpoint
# -----------------------------------
@app.get("/")
async def read_root():
    # Returns a simple greeting message
    return {"message": "Hello, World!"}


# -----------------------------------
# Pydantic Models (Request Body Schemas)
# -----------------------------------
class Item(BaseModel):
    name: str
    description: str
    price: float


class User(BaseModel):
    username: str
    first_name: str
    last_name: str
    email: str | None = None


# -----------------------------------
# PUT Endpoint with Path + Body Validation
# -----------------------------------
@app.put("/items/{item_id}/users/{user_id}")
async def update_item_user(
    *,     # Forces keyword-only arguments (better clarity & avoids mixups)

    item_id: int = Path(
        ...,
        title="Item ID",
        description="Item ID must be between 0 and 100.",
        ge=0,
        le=100
    ),

    user_id: int = Path(
        ...,
        title="User ID",
        description="User ID must be between 1 and 5000.",
        ge=1,
        le=5000
    ),

    item: Item | None = None,
    user: User | None = None,
    age: int = Body(
        ...,
        gt=0,
        lt=150,
        title="Age",
        description="Age must be between 1 and 149."
    )
):
    """
    Validates and updates:
    - item_id (0–100)
    - user_id (1–5000)
    - Item model (name, desc, price)
    - User model (username, first/last name, email)
    - Age (1–149)
    """

    return {
        "item_id": item_id,
        "user_id": user_id,
        "item": item,
        "user": user,
        "age": age
    }


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
