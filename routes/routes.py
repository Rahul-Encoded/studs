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
    