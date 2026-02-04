from fastapi import FastAPI, Path, Body
from pydantic import BaseModel, Field

app = FastAPI()


# -----------------------------------
# Root Endpoint
# -----------------------------------
@app.get("/")
async def read_root():
    # Returns a simple greeting message
    return {"message": "Hello, World!"}


# -----------------------------------
# Pydantic Model (Request Body Schema)
# -----------------------------------
class Item(BaseModel):
    name: str

    description: str | None = Field(
        default=None,
        description="The description of the item",
        max_length=300
    )

    price: float = Field(
        ...,
        gt=0,
        description="The price must be greater than zero"
    )

    tax: float | None = Field(
        default=None,
        description="The tax applied to the item (optional)"
    )


# -----------------------------------
# PUT Endpoint: Update Item
# -----------------------------------
@app.put("/items/{item_id}")
async def update_item(
    item_id: int = Path(
        ...,
        title="Item ID",
        description="The ID of the item to update. Must be ≥ 1.",
        ge=1
    ),

    item: Item = Body(
        ...,
        embed=True,
        description="The item data to update"
    )
):
    """
    Updates an item by ID.
    Validates:
    - item_id (must be ≥ 1)
    - item (validated by the Item BaseModel)
    """

    return {
        "item_id": item_id,
        "item": item
    }


# ---------------------------------------------------------
# WHY USE Field() WITH BaseModel?
# ---------------------------------------------------------
"""
Field() gives extra control over model attributes:

1) Add validation:
   price: float = Field(..., gt=0)
   → ensures price > 0

2) Add metadata for Swagger docs:
   description="The item description"

3) Add constraints:
   max_length=300

4) Set default values while still using validation:
   description: str | None = Field(default=None, max_length=300)

5) Makes documentation cleaner and more readable.

Summary:
--------
Use Field() when you want:
- validation
- description
- constraints
- Swagger docs metadata
- default values with structured control
"""
