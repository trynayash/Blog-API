from fastapi import FastAPI
from app.routes import blog_routes, user_routes
from bson import ObjectId
from pydantic import BaseModel


# Custom PyObjectId class for handling ObjectId with Pydantic v2
class PyObjectId(ObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, value):
        if not ObjectId.is_valid(value):
            raise ValueError("Invalid ObjectId")
        return ObjectId(value)

    @classmethod
    def __get_pydantic_json_schema__(cls, schema):
        schema.update(type="string")
        return schema


# BaseModel to handle MongoDB documents with ObjectId
class MongoBaseModel(BaseModel):
    id: PyObjectId

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}


# Initialize the FastAPI application
app = FastAPI()

# Include routers
app.include_router(blog_routes.router, prefix="/blogs", tags=["Blogs"])
app.include_router(user_routes.router, prefix="/users", tags=["Users"])

@app.get("/")
def read_root():
    return {"message": "Welcome to the School Blog API!"}
