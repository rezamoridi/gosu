from fastapi import FastAPI, Request                        # FastAPI
# allow to use static files
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
# Rendering Jinja2 templates
from fastapi.templating import Jinja2Templates

# Import Models
from models import StudentId

# Instance
app = FastAPI()

# Templates
auth_templates = Jinja2Templates(directory="../templates/auth")

# Mount the static files directory
app.mount("/statics", StaticFiles(directory="../statics"), name="auth.css")

# APIs

"""valid studentNumber
        Path Parameter"""


@app.get('/auth/{studentNumber}')
def valid_student_number(studentNumber):

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


""" query parameter """


@app.get("/auth/")
def valid_student_number_query(studentNumber):
    return  valid_student_number(studentNumber)
    


"""Post & request body"""


@app.post("/auth/")
def post_student_number(studentNumber: StudentId):
        return {"studentNumber": studentNumber}
