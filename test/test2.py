from pydantic import BaseModel

class Student(BaseModel):
    student_number : bool
    student_name : str
    student_birth  : int
    student_serial: int
    studen_province : str
    student_city : str
    student_addr: str
    student_post_add : int
    student_cellphone : int
    student_phone : int
    student_faculty : str
    student_feild : str
    student_marital : bool
    stuent_id : int

