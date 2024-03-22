from pydantic import Field,field_validator, BaseModel, validator
import re
from typing import Optional
from .dicto import states, states_cities
from .states import iran_states
import datetime
""""
            Class Models 
"""


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
    


#Name
class Name(BaseModel):
    name : str = Field(max_length=10, pattern=r'^[\u0600-\u06FF\s]+$') 

    @field_validator('name')
    @classmethod
    def valid_name(cls, v):
        forbiden_chars = '۱۲۳۴۵۶۷۸۹۰'
        for i in sorted(v, reverse=True):
            for j in forbiden_chars:
                if i == j:
                    raise ValueError("Name Error: Use only chars")
        return v



#Date
class BirthDate(BaseModel):
    date : datetime.date = Field(description="Must follow jalali date")

    @field_validator('date')
    def valid_date(cls, v):
        if v.year not in range (1320,1403):
            raise ValueError('Year must be at this range 1320-1403')
        
    
  

#SerialID
class SerialId(BaseModel):
    number : int = Field(ge=0, le=99999999)
    char: str = Field(min_length=1, max_length=1)

    @field_validator('number')
    @classmethod
    def valid_number(cls, v):
        str_v = str(v)
                                                                # FIX : input value doesnt have a good pattern
        if len(str_v) != 8:
            raise ValueError("Seria-ID lenght Error")
        return v
    
    @field_validator('char')
    @classmethod
    def valid_char(cls, v):
        if not re.match(pattern=r'^[\u0600-\u06FF\s]+$', string=v):
            raise ValueError("Serial-id Char Must be in persian alphba")
        return v
    



#State
class State(BaseModel):
    province: str = Field(min_length=2, max_length=25)
    city: Optional[str] = Field(min_length=2, max_length=25)


    @field_validator('province')
    @classmethod
    def valid_province(cls, v):
        if v not in states:
            raise ValueError('invaild provine')
        return v
    
    @field_validator('city')
    @classmethod
    def valid_city(cls, v, values):
        if values.data['province'] in states:
            if v not in  states_cities[values.data['province']] :
                raise ValueError("Wrong city")
        return v



#birth
class State(BaseModel):
    state: str = Field(min_length=3, max_length=20)

    @field_validator('state')
    @classmethod
    def valid_state(cls, v):
        if v not in iran_states:
            raise ValueError("Please insert a Valid State")
        return v

# city
class City(BaseModel):
    city : str = Field(min_length=1, max_length=25)

    @field_validator('city')
    @classmethod
    def valid_city(cls, v):
        cities =open("iranCities.csv", "r").read()

        persian_unicode = r'^[\u0600-\u06FF\s]+$'
        if not re.match(pattern=persian_unicode, string=v):
            raise ValueError("Use persian keywords")
        if v not in cities:
            raise ValueError("City not found")
        

# Postal code
class PostalCode(BaseModel):
    code: int = Field(gt=99999999, lt=10000000000)

# phone
class PhoneNumber(BaseModel):
    number : str =Field(min_length=11, max_length=11, pattern=r'^09')

    @field_validator('number')
    @classmethod
    def valid_state(cls,v):
        if not v:
            raise ValueError("invalid number")
        return v
    

# phone line

class PhoneLine(BaseModel):
    number : str = Field(min_length=8, max_length=8, pattern=r'^0')


# address
class Address(BaseModel):
    state: State
    city: City
    detail: str = Field(min_length=5, max_length=100)

    

# ID
class NationalID(BaseModel):
    number : int = Field(gt=99999999, lt=9999999999)
    

    @field_validator("number")
    @classmethod
    def valid_id(cls, v):
        def check_code_meli(code):
            code1 = str(code)
            L = len(code1)
        
            if L < 8 or int(code) == 0:
                return False
        
            code1 = ('0000' + code1)[-10:]
        
            if int(code1[3:9]) == 0:
                return False
        
            c = int(code1[9])
            s = 0
            for i in range(9):
                s += int(code1[i]) * (10 - i)
        
            s = s % 11
            return (s < 2 and c == s) or (s >= 2 and c == (11 - s))

        if not check_code_meli(v):
            raise ValueError("invalid code melli")
        return v

class Faculty(BaseModel):
    id : int = Field(gt=9, le=99)

    @validator('id')
    def valid_id(cls,v):
        if v not in [10,11,12,13,14,15,16,17,18,19,20,23,31,32,33,34,35,89,90]:
            raise ValueError("Invalid faculty")

class FieldOfStudy(BaseModel):
    id : int = Field(ge=10, le=19)

