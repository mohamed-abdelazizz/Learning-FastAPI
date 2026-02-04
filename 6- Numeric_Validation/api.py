from fastapi import FastAPI, Path, Query

app = FastAPI()


# -----------------------------------
# Root Endpoint
# -----------------------------------
@app.get("/")
async def read_root():
    # Returns a simple greeting message
    return {"message": "Hello, World!"}


# -----------------------------------
# Path Parameter Validation (item_id)
# -----------------------------------
@app.get("/items/{item_id}")
async def read_item(
    item_id: int = Path(
        ...,
        title="Item ID",
        description="The item_id must be between 1 and 1000.",
        ge=1,
        le=1000
    )
):
    """
    Validates "item_id":
    - Must be >= 1
    - Must be <= 1000
    """
    return {"item_id": item_id}


# -----------------------------------
# Query Parameter Validation (min_price & max_price)
# -----------------------------------
@app.get("/items")
async def read_items(
    min_price: float = Query(
        ...,
        title="Minimum Price",
        description="The minimum price must be greater than 0.",
        gt=0
    ),
    max_price: float = Query(
        ...,
        title="Maximum Price",
        description="The maximum price must be less than 1000.",
        lt=1000
    )
):
    """
    Validates:
    - min_price > 0
    - max_price < 1000
    """
    return {
        "min_price": min_price,
        "max_price": max_price
    }
    
