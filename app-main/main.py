from fastapi import FastAPI, Request, HTTPException        # FastAPI
# allow to use static files
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
# Rendering Jinja2 templates
from fastapi.templating import Jinja2Templates
from pydantic import ValidationError, BaseModel
# Import Models
from models import Student, StudentNumber


# Instance
app = FastAPI()

# Templates
auth_templates = Jinja2Templates(directory="../templates/auth")

# Mount the static files directory
app.mount("/statics", StaticFiles(directory="../statics"), name="auth.css")



#validator
def student_number_validator(number):
    try:
        student_numb = StudentNumber(student_number=number)
        return student_numb
    except ValidationError as e:
        # Return a custom HTTPException with status code 400 (Bad Request)
        # and provide details about the validation error
        #error_message = e.errors()[0]['msg']
        raise HTTPException(status_code=400, detail= e.errors()[0]["msg"])



# APIs

"""valid studentNumber
        Path Parameter"""

@app.get("/{studentNumber}", response_model=StudentNumber)
def valid_sn_path(studentNumber: int):
    student_number_validator(studentNumber)

"""valid studentNumber
        Query Parameter"""

@app.get("/", response_model=StudentNumber)
def valid_sn_query(studentNumber: int):
    student_number_validator(studentNumber)

"""valid studentNumber
        Post Body"""

@app.post("/", response_model=StudentNumber)
def post_student_number(studentNumber: StudentNumber):
    try:
        return studentNumber
    except ValidationError as e:
        raise HTTPException(status_code=400, detail=e.errors()[0]["msg"])