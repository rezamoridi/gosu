"""@app.get("/", response_class=HTMLResponse)
async def show_form(request: Request):
    # Render the HTML form
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/calculate", response_class=HTMLResponse)
async def calculate(request: Request, num1: float, num2: float, operation: str):
    result = None
    if operation == "add":
        result = num1 + num2
    elif operation == "subtract":
        result = num1 - num2
    elif operation == "multiply":
        result = num1 * num2
    elif operation == "divide":
        if num2 != 0:
            result = num1 / num2
        else:
            return templates.TemplateResponse(request=request, name="index.html" ,error_message="Cannot divide by zero!")
    return templates.TemplateResponse(request=request, name="index.html")"""