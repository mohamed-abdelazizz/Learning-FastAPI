from fastapi import FastAPI, Path, Body
from pydantic import BaseModel, HttpUrl, Field

app = FastAPI()


# -----------------------------------
# Root Endpoint
# -----------------------------------
@app.get("/")
async def read_root():
    # Returns a simple greeting message
    return {"message": "Hello, World!"}


# -----------------------------------
# Pydantic Models
# -----------------------------------
class Image(BaseModel):
    url: HttpUrl = Field(..., description="Valid URL for the image")
    description: str | None = Field(
        default=None,
        description="Optional description of the image"
    )


class Item(BaseModel):
    name: str = Field(..., description="Name of the item")
    description: str | None = Field(
        default=None,
        description="Optional description of the item"
    )
    price: float = Field(..., gt=0,
                         description="Price must be greater than zero")
    image: Image = Field(..., description="Image details of the item")


class Product(BaseModel):
    image: Image = Field(..., description="Image of the product")
    item: Item = Field(..., description="Item details inside the product")


# -----------------------------------
# PUT: Update Item
# -----------------------------------
@app.put("/products/{item_id}")
async def update_product(
    item_id: int = Path(
        ...,
        ge=1,
        title="Item ID",
        description="The ID of the item to update. Must be ≥ 1."
    ),
    item: Item = Body(..., description="The updated item data")
):
    """
    Updates an item by ID.\n
    Validates:
    - item_id (must be >= 1)
    - item (validated using Item BaseModel)
    """
    return {
        "item_id": item_id,
        "item": item
    }


# -----------------------------------
# POST: Create Product
# -----------------------------------
@app.post("/products/{product_id}")
async def create_product(
    product_id: int = Path(
        ...,
        ge=1,
        title="Product ID",
        description="The product ID. Must be ≥ 1."
    ),
    product: Product = Body(..., description="The full product data")
):
    """
    Creates a new full Product.\n
    Product includes:
    - image (Image Model)
    - item  (Item Model)
    """
    return {
        "product_id": product_id,
        "product": product
    }


# -----------------------------------
# Why Use HttpUrl?
# -----------------------------------
"""
- Automatically validates strings to ensure they are proper URLs.
- Prevents invalid or malformed URLs.
- No need to manually write regex for URLs.
"""
