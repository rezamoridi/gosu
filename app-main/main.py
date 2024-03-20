from fastapi import FastAPI, Request, HTTPException        # FastAPI
from persiantools.jdatetime import JalaliDate
# allow to use static files
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
# Rendering Jinja2 templates
from fastapi.templating import Jinja2Templates
from pydantic import ValidationError
# Import Models
from models import StudentNumber, Name, Date


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