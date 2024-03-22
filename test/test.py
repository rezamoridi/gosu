from typing import Union, Optional
from pydantic import BaseModel, field_validator, ValidationError
import uuid

# studentNumber

class StudentNumber(BaseModel):
    year : int
    const : int = None
    andis  : int = None

    @field_validator('year')
    @classmethod
    def valid_year(cls, v):
        if v not in [400, 401, 402]:
            raise ValueError("Year Part is Wrong")
        return v
    
    @field_validator('const')
    @classmethod
    def valid_const(cls, v):
        if v != 114150:
            raise ValueError("Const Part is Wrong")
        return v

    @field_validator('andis')
    @classmethod
    def valid_andis(cls, v):
        if v not in range(0,100):
            raise ValueError("Andis is Wrong")
        return v



    

# global user
class User(BaseModel):
    username : str = "visitor"
    name : str  = "user"
    email : str = "example@gmail.com"
    phone_line: int = 0
    phone_landline: str = None
    address : str = None
    id_number : int = 0
    id_serial : str = 0

    @field_validator('name')
    @classmethod
    def valid_name(cls, v):
        if v == 'reza':
            raise ValueError("Use only chars")
        return v
    
# Student of Uni
class Student(User):
    student_number: str
    field_of_study : str
    faculty: str
    is_mirage: bool
    is_active : bool
        
# Lecturer of Uni
class Lecturer(User):
    lecturer_number: str
    id_number: str
    is_active: bool

r1 = User(name='reza')