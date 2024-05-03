from pydantic import BaseModel, field_validator, validator
from defined_classes import *
""""
            Users Models 
"""

class User(BaseModel):
    name : Name
    username : str = "visitor"
    birthdate : BirthDate
    email : str = "example@gmail.com"
    phone_number: PhoneNumber = None
    phone_landline: PhoneLine = None
    id_number : PID 
    id_serial : SerialId 

    
# Student of Uni
class Student(User):
    student_number: StudentNumber
    field_of_study : FieldOfStudy
    birth_city : City
    birth_state : State
    address : Address
    faculty: Faculty
    is_mirage: bool
    is_active : bool





        
# Lecturer of Uni
class Lecturer(User):
    lecturer_number: str
    id_number: str
    is_active: bool


