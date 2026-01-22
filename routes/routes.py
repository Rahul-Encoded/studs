from fastapi import APIRouter
from models.users import User
from config.dbconfig import collection_name
from schema.users import list_serial
from bson import ObjectId

endpoints = APIRouter()

@endpoints.get("/")
def home():
    return{
        "status": "OK",
        "message": "My fast api is running"
    }

@endpoints.get("/v1/users")
async def get_users():
    users = list_serial(collection_name.find())
    return users 

@endpoints.post("/v1/users")
async def post_user(user: User):
    collection_name.insert_one(dict(user))
    return {
        "status": "OK",
        "message": "User created successfully"
    }

@endpoints.put("/v1/users/{id}")
async def update_user(user: User, id: str):
    collection_name.find_one_and_update({"_id": ObjectId(id)}, {"$set": dict(user)})
    return {
        "status": "OK",
        "message": "User updated successfully"
    }

@endpoints.delete("/v1/users/{id}")
async def delete_user(id: str):
    collection_name.find_one_and_delete({"_id": ObjectId(id)})
    return {
        "status": "OK",
        "message": "User deleted successfully"
    }