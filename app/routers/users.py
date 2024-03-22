from fastapi import HTTPException, APIRouter, Body
from pydantic import ValidationError
from schemas import users as schemas

router = APIRouter()

"""valid Student
        POST"""
@router.post('/student/', response_model=schemas.Student)
def valid_student(student: schemas.Student = Body(...)):
    try:
        return student
    except ValidationError as e:
        HTTPException(status_code=400, detail=e.errors)
