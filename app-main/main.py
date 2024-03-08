from fastapi import FastAPI, Request, HTTPException        # FastAPI
# allow to use static files
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
# Rendering Jinja2 templates
from fastapi.templating import Jinja2Templates
from pydantic import ValidationError
# Import Models
from models import Student, StudentNumber


# Instance
app = FastAPI()

# Templates
auth_templates = Jinja2Templates(directory="../templates/auth")

# Mount the static files directory
app.mount("/statics", StaticFiles(directory="../statics"), name="auth.css")

# APIs

"""valid studentNumber
        Path Parameter"""

@app.get("/auth/{studentNumber}")
def p_student_number_auth(studentNumber: int):
    try:
        StudentNumber(student_number=studentNumber)
        return int(studentNumber)
    except ValidationError as e:
        # Return a custom HTTPException with status code 400 (Bad Request)
        # and provide details about the validation error
        error_message = e.errors()[0]['msg']
        raise HTTPException(status_code=400, detail=error_message)