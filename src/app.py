from fastapi import FastAPI
from fastapi.responses import HTMLResponse


app = FastAPI()


@app.get("/")
def investments() -> HTMLResponse:
    with open("static/investments-app.html") as f:
        return f.read() 