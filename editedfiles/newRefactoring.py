from fastapi import FastAPI
from typing import Callable

app = FastAPI()

# Utility functions for validation
def validate_password(password: str):
    if len(password) < 8:
        raise ValueError("Password too short")

def validate_email(email: str):
    if "@" not in email:
        raise ValueError("Invalid email")

# Centralized validation function
def validate_user_data(email: str, password: str):
    validate_email(email)
    validate_password(password)

@app.post("/users/")
async def create_user(name: str, email: str, password: str):
    try:
        validate_user_data(email, password)
    except ValueError as e:
        return {"error": str(e)}
    return {"name": name, "email": email}

@app.put("/users/")
async def update_user(name: str, email: str, password: str):
    try:
        validate_user_data(email, password)
    except ValueError as e:
        return {"error": str(e)}
    return {"name": name, "email": email}
