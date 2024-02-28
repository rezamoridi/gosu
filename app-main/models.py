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
