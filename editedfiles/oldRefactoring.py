from fastapi import FastAPI

app = FastAPI()

@app.post("/users/")
async def create_user(name: str, email: str, password: str):
    if len(password) < 8:
        raise ValueError("Password too short")
    if "@" not in email:
        raise ValueError("Invalid email")
    return {"name": name, "email": email}

@app.put("/users/")
async def update_user(name: str, email: str, password: str):
    if len(password) < 8:
        raise ValueError("Password too short")
    if "@" not in email:
        raise ValueError("Invalid email")
    return {"name": name, "email": email}