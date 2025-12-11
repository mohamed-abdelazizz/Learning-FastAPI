from fastapi import FastAPI

app = FastAPI()


# ---------------------------
# HTTP Methods Endpoints
# ---------------------------
@app.get("/", description="GET endpoint")
async def get_fun():
    # Retrieves data (non-modifying)
    return {"message": "This is GET request"}


@app.post("/", description="POST endpoint")
async def post_fun():
    # Creates new data
    return {"message": "This is POST request"}


@app.put("/", description="PUT endpoint", deprecated=True)
async def put_fun():
    # Updates/replaces data
    # Marked as deprecated
    return {"message": "This is PUT request"}


# ---------------------------
# HTTP Methods Summary
# ---------------------------
"""
Idempotent = sending the same request multiple times gives the same final result.

1) GET:
    - Retrieve data from the server
    - Should not modify data
    - Idempotent

2) POST:
    - Create new data
    - Sends data in request body
    - Not idempotent (repeating creates duplicates)

3) PUT:
    - Update/replace existing data
    - Requires sending full object
    - Idempotent
"""


# ---------------------------
# FastAPI Core Concepts
# ---------------------------
"""
1) Starlette:
    - FastAPI is built on top of Starlette.
    - FastAPI adds automatic docs and validation using Pydantic.
    - Starlette provides core web features:
        * Routing
        * Middleware
        * Requests & Responses
        * Background tasks
        * WebSockets

2) Pydantic:
    - Used for:
        * Data validation
        * Type checking
        * Type conversion
    - Models are created using Pydantic BaseModel

3) Uvicorn:
    - ASGI server to run FastAPI
    - Command: uvicorn api:app --reload
"""


# ---------------------------
# Async / Await Summary
# ---------------------------
"""
1) async:
    - Makes the function asynchronous (non-blocking).
    - Allows the server to handle other requests while waiting.
    - Useful for operations that take time:
        * Database queries
        * External API calls
        * File reading/writing
        * Network I/O

2) await:
    - Used inside async functions.
    - Tells Python to "pause" this task without blocking the server.
    - While waiting, the server can serve other requests.

Why async in FastAPI?
    - FastAPI is built to be asynchronous.
    - Using async improves performance and allows high concurrency.
    - The API can handle many clients at the same time, even during slow operations.

Summary:
    async = function can run without blocking
    await = wait without stopping the whole application server. 
            pause this task, continue others in the meantime
"""


# ---------------------------
# Deprecated Endpoints
# ---------------------------
"""
deprecated=True:
    - Marks an endpoint as outdated / to be removed in future
    - Shows a warning in Swagger UI
    - Useful to inform users (dev) to switch to a new endpoint.
"""
