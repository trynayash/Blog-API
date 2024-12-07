from fastapi import APIRouter, HTTPException
from app.models.user import User
from app.services.database import db

router = APIRouter()

@router.get("/")
async def get_users():
    users = await db["users"].find().to_list(100)
    return users

@router.post("/")
async def create_user(user: User):
    user_dict = user.dict()
    result = await db["users"].insert_one(user_dict)
    return {"id": str(result.inserted_id)}
