from fastapi import FastAPI

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
    {"id": 6, "name": "game", "price": "10", "stock": True},
]


# ---------------------------
# Items with Filters + Pagination
# ---------------------------
@app.get("/items")
async def get_items(
    start: int = 0,
    end: int = 10,
    id: int = None,
    name: str = None
):
    # Filter: item by ID
    if id:
        item = next((item for item in items if item["id"] == id), None)
        return item if item else {"message": "Item not found"}

    # Filter: items by name
    if name:
        filtered_items = [item for item in items if item["name"] == name]
        return filtered_items

    # Pagination results
    return items[start:start + end]


# ---------------------------
# Sort Items by Price + Optional Range Filtering
# ---------------------------
@app.get("/items/prices")
async def get_items_by_price(max_range: str = None):
    # Sort items by price (descending)
    sorted_items = sorted(items, key=lambda x: int(x["price"]), reverse=True)

    # Optional: filter by maximum price
    if max_range:
        try:
            max_price = int(max_range)
        except ValueError:
            return {"error": "Invalid max_range value. Please provide a numeric value."}
        filtered_items = [item for item in sorted_items if int(
            item["price"]) <= max_price]
        return filtered_items

    return sorted_items


# ---------------------------
# Filter Items by Stock Availability
# ---------------------------
@app.get("/items/stock")
async def get_items_by_stock(in_stock: bool = True):
    """
    - in_stock=True  → return only items in stock
    - in_stock=False → return only out-of-stock items
    """

    if in_stock:
        stock_items = [item for item in items if item["stock"]]
        return stock_items

    out_of_stock_items = [item for item in items if not item["stock"]]
    return out_of_stock_items
