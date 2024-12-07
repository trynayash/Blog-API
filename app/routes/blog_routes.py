from fastapi import APIRouter, HTTPException
from app.models.blog import Blog
from app.services.database import db

router = APIRouter()

@router.get("/")
async def get_blogs():
    blogs = await db["blogs"].find().to_list(100)
    return blogs

@router.post("/")
async def create_blog(blog: Blog):
    blog_dict = blog.dict()
    result = await db["blogs"].insert_one(blog_dict)
    return {"id": str(result.inserted_id)}
