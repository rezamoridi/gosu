from fastapi import FastAPI, Request, HTTPException        # FastAPI
from persiantools.jdatetime import JalaliDate
# allow to use static files
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
# Rendering Jinja2 templates
from fastapi.templating import Jinja2Templates
from pydantic import ValidationError
# Import Models
from defined_classes import StudentNumber, Name, Date, SerialId, State, PhoneNumber, PhoneLine, Address, PID


# Instance
app = FastAPI()


# Mount the static files directory
app.mount("/statics", StaticFiles(directory="../statics"), name="style.css")
# Templates
templates = Jinja2Templates(directory="../templates/test")


# APIs

"""@app.get("/", response_class=HTMLResponse)
async def show_form(request: Request):
    # Render the HTML form
    return templates.TemplateResponse(request=request, name="index.html")""" # Template -< 


"""valid studentNumber
        Path Parameter"""


@app.get("/{studentNumber}", response_model=StudentNumber)
def valid_sn_path(studentNumber: int):
    try:
        return StudentNumber(student_number=studentNumber)
    except ValidationError as e:
        raise HTTPException(status_code=400, detail=str(e))


"""valid studentNumber
        Query Parameter"""


@app.get("/", response_model=StudentNumber)
def valid_sn_query(studentNumber: int):
    try:
        return StudentNumber(student_number=studentNumber)
    except ValidationError as e:
        raise HTTPException(status_code=400, detail=str(e))


"""valid studentNumber
        Post Body"""


@app.post("/", response_model=StudentNumber)
def post_student_number(studentNumber: StudentNumber):
    try:
        return studentNumber
    except ValidationError as e:
        raise HTTPException(status_code=400, detail=e.errors()[0]["msg"])
    

"""valid name
        POST"""


@app.post("/name/", response_model=Name)
def valid_name(name: Name):
    try:
        return name
    except ValidationError as e:
        raise HTTPException(status_code=400, detail=e.errors)
    

"""valid date
        POST"""


@app.post("/date/", response_model=Date)
def valid_date(date: Date):
    try:
        return date
    except ValidationError as e:
        raise HTTPException(status_code=400, detail=e.errors)


"""valid Serial ID
        POST"""


@app.post("/serial-id/", response_model=SerialId)
def valid_serial(serial_id: SerialId):
    try:
        return serial_id
    except ValidationError as e:
        raise HTTPException(status_code=400, detail=e.errors)


""" valid State
        POST"""

@app.post("/state/", response_model=State)
def valid_state(state: State):
    try:
        return state
    except ValidationError as e:
        raise HTTPException(status_code=400, detail=e.errors)



""" valid city
        POST"""

@app.post("/city")
def valid_city(city):
    return True


""" valid address
        POST"""

@app.post('/address')
def valid_address(address:Address):
    try:
        return Address
    except ValidationError as e:
        return HTTPException(status_code=400, detail=e.errors)


""" valid Postal code
        POST"""

@app.post("/postal_code/")
def valid_postal_code(code):
    return True


"""valid phone number
        POST"""

@app.post("/phonenumber/", response_model=PhoneNumber)
def valid_phone_number(number: PhoneNumber):
    try:
        return number
    except ValidationError as e:
        raise HTTPException(status_code=400, detail=e.errors)
    
"""valid phone line
        POST"""

@app.post("/phoneline/", response_model=PhoneLine)
def valid_phone_line(phoneline: PhoneLine):
    try:
        return phoneline
    except ValidationError as e:
        raise HTTPException(status_code=400, detail=e.errors)
    

""" valid faculty
        POST"""

@app.post("/faculty")
def valid_faculty(faculty):
        return True


""" marriage status
        POST"""

@app.post("/marriage/")
def marriage_status(status):
    return True

""" valid ID
        POST"""

@app.post("/id/", response_model=PID)
def valid_id(id:PID):
    try:
        return id
    except ValidationError as e:
        return HTTPException(status_code=400, detail=e.errors)