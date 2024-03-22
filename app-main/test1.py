"""
    This File is for testing front-end part and exercising templating 
"""


from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates 
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse

app = FastAPI() # App instance 

templates = Jinja2Templates(directory="../templates/tesst")  # Template Instance 
app.mount("/statics", StaticFiles(directory="../statics"), name="style.css") # Mount statics

""" API
    Methods""" 


@app.get("/", response_class=HTMLResponse)
def templ(request: Request):
    return templates.TemplateResponse(request=request, name="test_index.html")

@app.post("/", response_class=HTMLResponse)
async def calculate(request: Request, num1: float, num2: float, operation: str):
    result = None
    if operation == 'add':
        result = num1 + num2
    elif operation == 'subtract':
        result = num1 - num2
    elif operation == 'multiply':
        result = num1 * num2
    elif operation == 'divide':
        if num2 != 0:
            result = num1 / num2
        else:
            result = "Error: Cannot divide by zero"
    return templates.TemplateResponse("test_indext.html", {"request": request, "result": result})

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)