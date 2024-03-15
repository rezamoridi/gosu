from pydantic import BaseModel, field_validator, Field
import uuid

# studentNumber
class StudentNumber(BaseModel):
    student_number: int

    def __str__(cls):
        return f"{cls.student_number}"

    @field_validator('student_number')
    @classmethod
    def valid_year(cls, number):
        number_str = str(number)
        if len(number_str) != 11:
            raise ValueError("Studen Number must have 11 Digits")
        if number_str[:3] not in ['400', '401', '402']:
            raise ValueError("Student Number Year Part is not correct")
        if number_str[3:9] != "114150":
            raise ValueError("Student Number Const Part is Wrong")
        if int(number_str[9:12]) not in range(0,100):
            raise ValueError("Student Number Andis Part is Wrong") 
        return number
    
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
    student_number: StudentNumber
    field_of_study : str
    faculty: str
    is_mirage: bool
    is_active : bool
        
# Lecturer of Uni
class Lecturer(User):
    lecturer_number: str
    id_number: str
    is_active: bool
