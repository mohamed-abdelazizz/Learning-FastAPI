from fastapi import FastAPI
from enum import Enum

app = FastAPI()


# ---------------------------
# Simple GET endpoint
# ---------------------------
@app.get("/users")
async def get_users():
    # Returns a simple list of users
    return {"message": "List of users"}


# ---------------------------
# Static path before dynamic
# ---------------------------
# include_in_schema=False hides this endpoint from Swagger docs to be secure it.
# Useful for sensitive/admin endpoints
@app.get("/users/1", include_in_schema=False)
async def admin_user():
    return {"message ": "this is the admin portal"}


# ---------------------------
# Dynamic path parameter
# ---------------------------
@app.get("/users/{user_id}")
async def get_user(user_id: int):
    # user_id is captured from the path as an integer
    return {"message": f"User with ID {user_id}"}


# ---------------------------
# Enum usage for path parameter
# ---------------------------
class UserRole(str, Enum):
    admin = "admin"
    editor = "editor"
    viewer = "viewer"


@app.get("/users/role/{role}/{user_id}")
async def get_user_by_role(role: UserRole, user_id: int):
    # user_type must be one of the enum values (admin, editor, viewer)
    # user_id can be any valid integer
    # Returns a dict with user type and id
    return {"message": f"User with ID {user_id} has role {role}"}


"""
Summary Notes:
---------------
1) Static routes should come BEFORE dynamic routes to avoid conflicts.
2) include_in_schema=False hides endpoints from automatic docs to be secure.
3) Enum classes are useful to restrict path parameter values.
"""
