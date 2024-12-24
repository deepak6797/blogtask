# main.py

from fastapi import FastAPI, HTTPException, Depends
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from models import Post, PostUpdate
from typing import List

app = FastAPI()

# Serve static files (CSS, JS, etc.)
app.mount("/static", StaticFiles(directory="static"), name="static")

# In-memory "database"
posts_db = {}

@app.get("/", response_class=HTMLResponse)
async def read_root():
    # Serve the frontend HTML
    with open("templates/index.html", "r") as file:
        return file.read()

@app.post("/posts/", response_model=Post)
async def create_post(post: Post):
    # Check if the title already exists
    if post.title in posts_db:
        raise HTTPException(status_code=400, detail="Post with this title already exists.")
    posts_db[post.title] = post
    return post

@app.get("/posts/", response_model=List[Post])
async def get_posts():
    return list(posts_db.values())

@app.put("/posts/{title}", response_model=Post)
async def update_post(title: str, post_update: PostUpdate):
    if title not in posts_db:
        raise HTTPException(status_code=404, detail="Post not found.")
    
    existing_post = posts_db[title]
    updated_post = existing_post.copy(update=post_update.dict(exclude_unset=True))
    posts_db[title] = updated_post
    return updated_post

@app.delete("/posts/{title}", response_model=Post)
async def delete_post(title: str):
    if title not in posts_db:
        raise HTTPException(status_code=404, detail="Post not found.")
    
    deleted_post = posts_db.pop(title)
    return deleted_post
