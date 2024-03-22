from pydantic import BaseModel
from defined_classes import Date, StudentNumber, SerialId, Name

        
""""
            Users Models 
"""

class User(BaseModel):
    name : Name
    username : str = "visitor"
    birthdate : Date
    email : str = "example@gmail.com"
    phone_line: int = 0
    phone_landline: str = None
    address : str = None
    id_number : int = 0
    id_serial : SerialId = 0

    
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


