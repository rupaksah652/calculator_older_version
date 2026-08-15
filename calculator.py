from fastapi import FastAPI,Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel,Field
from typing import Annotated

app=FastAPI()
MODEL_VERSION='2.0.0'

# Static files
app.mount("/static", StaticFiles(directory="static"), name="static")

# HTML templates
templates = Jinja2Templates(directory="templates")

class UserInput(BaseModel):
    a:Annotated[float,Field(...,description='give the data/values of a')]
    b:Annotated[float,Field(...,description='give the data/values of b')]
    choice:Annotated[int,Field(...,description="1.Add , 2.Subtract , 3.Multiply , 4.Division ")]

#website
@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse(request=request,
        name="index.html",
        context={})

#claculator status
@app.get('/calculator_status')
def claculator_check():
    return{
        'status':'OK',
        'version':MODEL_VERSION,
    }

#calculator API
@app.post('/calculator')
def calculator(data:UserInput):
 
    if data.choice == 1:
        result = data.a + data.b
        operation = 'Addition'

    elif data.choice == 2:
        result = data.a - data.b
        operation = 'Subtraction'

    elif data.choice == 3:
        result = data.a * data.b
        operation = 'Multiplication'

    elif data.choice == 4:
        if data.b == 0:
            return {'error':'canot divide by 0'}
        result = data.a / data.b
        operation = 'Division'
    
    else:
        return {'error':'invalid choice,please choose 1 , 2 , 3 , or 4'}

    return {
        'a' : data.a,
        'b' : data.b,
        'operation': operation,
        'result': result
    }

      


