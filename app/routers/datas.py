from fastapi import HTTPException, APIRouter
from pydantic import ValidationError
from schemas import Schemas


router = APIRouter()

"""valid studentNumber
        Path Parameter"""

@router.get("/{studentNumber}", response_model=Schemas.StudentNumber)
def valid_sn_path(studentNumber: int):
    try:
        return Schemas.StudentNumber(student_number=studentNumber)
    except ValidationError as e:
        raise HTTPException(status_code=400, detail=str(e))


"""valid studentNumber
        Query Parameter"""


@router.get("/", response_model=Schemas.StudentNumber)
def valid_studentnumber_query(studentNumber: int):
    try:
        return Schemas.StudentNumber(student_number=studentNumber)
    except ValidationError as e:
        raise HTTPException(status_code=400, detail=str(e))


"""valid studentNumber
        Post Body"""


@router.post("/", response_model=Schemas.StudentNumber)
def post_student_number(studentNumber: int):
    try:
        return Schemas.StudentNumber(student_number=studentNumber)
    except ValidationError as e:
        raise HTTPException(status_code=400, detail=e.errors()[0]["msg"])
    

"""valid name
        POST"""


@router.post("/name/", response_model=Schemas.Name)
def valid_name(name: str):
    try:
        return name
    except ValidationError as e:
        raise HTTPException(status_code=400, detail=e.errors)
    

"""valid date
        POST"""


@router.post("/BirthDate/", response_model=Schemas.BirthDate)
def jalaliDate(birthdate: Schemas.BirthDate):
    try:
        return birthdate
    except ValidationError as e:
        raise HTTPException(status_code=400, detail=e.errors)


"""valid Serial ID
        POST"""


@router.post("/serial-id/", response_model=Schemas.SerialId)
def valid_serial(serial_id: Schemas.SerialId):
    try:
        return serial_id
    except ValidationError as e:
        raise HTTPException(status_code=400, detail=e.errors)


""" valid State
        POST"""

@router.post("/state/", response_model=Schemas.State)
def valid_state(state: Schemas.State):
    try:
        return state
    except ValidationError as e:
        raise HTTPException(status_code=400, detail=e.errors)



""" valid city
        POST"""

@router.post("/city")
def valid_city(city: Schemas.City):
    try:
        return city
    except ValidationError as e:
        return HTTPException(status_code=400, detail=e.errors)


""" valid address
        POST"""

@router.post('/address', response_model=Schemas.Address)
def valid_address(address:Schemas.Address):
    try:
        return address
    except ValidationError as e:
        return HTTPException(status_code=400, detail=e.errors)


""" valid Postal code
        POST"""

@router.post("/postal_code/")
def valid_postal_code(postal_code: Schemas.PostalCode):
    try:
        return postal_code
    except ValidationError as e:
        return HTTPException(status_code=400, detail=e.errors)


"""valid phone number
        POST"""

@router.post("/phonenumber/", response_model=Schemas.PhoneNumber)
def valid_phone_number(number: Schemas.PhoneNumber):
    try:
        return number
    except ValidationError as e:
        raise HTTPException(status_code=400, detail=e.errors)
    
"""valid phone line
        POST"""

@router.post("/phoneline/", response_model=Schemas.PhoneLine)
def valid_phone_line(phoneline: Schemas.PhoneLine):
    try:
        return phoneline
    except ValidationError as e:
        raise HTTPException(status_code=400, detail=e.errors)
    

""" valid faculty
        POST"""

@router.post("/faculty")
def valid_faculty(faculty: Schemas.Faculty):
    try:
        return faculty
    except ValidationError as e:
        return HTTPException(status_code=400, detail=e.errors)
    

"""valid field of study
        POST"""

@router.post('/field/')
def valid_field(field: Schemas.FieldOfStudy):
    try:
        return field
    except ValidationError as e:
        return HTTPException(status_code=400, detail=e.errors)


""" marriage status
        POST"""

@router.post("/marriage/")
def marriage_status(status: bool):
    return status

""" valid ID
        POST"""

@router.post("/id/", response_model=Schemas.NationalID)
def valid_id(id:Schemas.NationalID):
    try:
        return id
    except ValidationError as e:
        return HTTPException(status_code=400, detail=e.errors)
    