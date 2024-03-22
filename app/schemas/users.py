from pydantic import BaseModel
from models import data as models
""""
            Users Models 
"""

class User(BaseModel):
    name : models.Name
    username : str = "visitor"
    birthdate : models.BirthDate
    email : str = "example@gmail.com"
    phone_number: models.PhoneNumber = None
    phone_landline: models.PhoneLine = None
    id_number : models.NationalID
    id_serial : models.SerialId 


# Student of Uni
class Student(User):
    student_number: models.StudentNumber
    field_of_study : models.FieldOfStudy
    birth_city : models.City
    birth_state : models.State
    address : models.Address
    faculty: models.Faculty
    is_mirage: bool
    is_active : bool





        
# Lecturer of Uni
class Lecturer(User):
    lecturer_number: str
    id_number: str
    is_active: bool


