from fastapi import FastAPI, Query

app = FastAPI()


# -----------------------------------
# Root Endpoint
# -----------------------------------
@app.get("/")
async def read_root():
    # Returns a simple greeting message
    return {"message": "Hello, World!"}


# -----------------------------------
# Basic Query Parameter (Optional)
# -----------------------------------
@app.get("/items")
async def read_items(name: str = "Unknown"):
    return {"name": name}


# -----------------------------------
# Validation with Query(...)
# -----------------------------------
@app.get("/validate")
async def validate_item(
    name: str = Query(
        ...,
        min_length=3,
        max_length=50,
        regex=r"^[a-zA-Z]+$",
        description="Name must contain only letters (3–50 chars)"
    ),
    email: str = Query(
        ...,
        min_length=5,
        max_length=100,
        regex=r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$",
        description="Valid email format required"
    )
):
    """
    Validates:
    - Name (letters only, length 3–50)
    - Email (must be a valid email format)
    """
    return {"Name": name, "Email": email}
