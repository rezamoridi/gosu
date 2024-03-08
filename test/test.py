# import mudols
from pydantic import BaseModel, conint, constr
from fastapi import FastAPI

# Models      
class StudentNumberModel(BaseModel):
    student_number : int

    def __init__(self, studentNumber):
        self.student_number = str(studentNumber)
    
    def isvalid(self):
        if len(self.student_number) != 11:
            return "ERROR 1 : Student Number Must Be 11 Digits"
        if self.student_number[:3] not in ['400', '401', '402']:
            return "ERROR 2: Studdent Number Year Part Is Not Correct"
        if self.student_number[3:10] != "114150":
            return "ERROR 3: Student Number Const Part Is Not Correct"
        if int(self.student_number[-2:]) not in range(0,100):
            return "ERROR 4: Student Number Andis Is Not Correct"
        
        return int(self.student_number)

class Id(BaseModel, StudentNumberModel):
    n : int