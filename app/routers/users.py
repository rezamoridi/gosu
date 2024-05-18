from fastapi import HTTPException, APIRouter, Body
from pydantic import ValidationError
from schemas import Schemas
from models import Models

from config import db


router = APIRouter()

"""valid Student
        POST"""
@router.post('/student/', response_model=Schemas.Student)
def valid_student(student: Schemas.Student = Body(...)):
    try:
        return student
    except ValidationError as e:
        HTTPException(status_code=400, detail=e.errors)


"""create UserInDB
"""
users_collection = db.users

@router.post("/user/", response_model=Models.UserInDB)
def create_user(user: Schemas.User):
    user_dict = user.model_dump()
    result = users_collection.insert_one(user_dict)
    user_in_db = Models.UserInDB(id=str(result.inserted_id), **user_dict)
    return user_in_db

@router.get("/users/", response_model=list[Models.UserInDB])
def get_users():
    users = list(users_collection.find())
    return [Models.UserInDB(id=str(user["_id"]), name=user["name"], email=user["email"]) for user in users]
