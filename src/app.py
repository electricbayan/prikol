from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles


app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")


templates = Jinja2Templates(directory="static")

@app.get("/")
def investments(request: Request) -> HTMLResponse:
    return templates.TemplateResponse("investment-app.html", {"request": request})
    # with open("/app/static/investment-app.html") as f:
    #     return f.read() 