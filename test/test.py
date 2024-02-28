@app.get('/auth/test/{studentNumber}')
def valid_student_number(studentNumber: int):

    if len(studentNumber) != 11:
        return "error : Student Number Must Be 11 Digits"
    else:
        if studentNumber[:3] not in ['400', '401', '402']:
            return "error : Student Number Year Part is not valid"
        if studentNumber[3:9] != '114150':
            return "error : Student Number Const Part Is Not Valid"
        if int(studentNumber[-1:]) not in range(0, 100):
            return "error: Student Number Last part is not valid"
        return int(studentNumber)
    

"""______________________________________________________________________________________________"""

from fastapi import FastAPI
from pydantic import BaseModel, constr, validator

# models

# studentNumber


class StudentId(BaseModel):
    studentNumber: constr

    @validator('studentNumber')
    def check_length(cls, v):
        if len(v) != 11:
            raise ValueError('Student number must be 11 digits long')
        return v

    @validator('studentNumber')
    def check_prefix(cls, v):
        prefix = v[:3]
        if prefix not in ('400', '401', '402'):
            raise ValueError('First 3 digits must be 400, 401, or 402')
        return v

    @validator('studentNumber')
    def check_middle(cls, v):
        middle = v[3:9]
        if middle != '114150':
            raise ValueError('Middle 6 digits must be 114150')
        return v

    @validator('studentNumber')
    def check_range(cls, v):
        last_two = int(v[9:])
        if not 1 <= last_two <= 99:
            raise ValueError('Last 2 digits must be in the range [01, 99]')
        return v
