# Данный модуль создает модель FastAPI

from fastapi import FastAPI
from starlette.staticfiles import StaticFiles
from starlette.templating import Jinja2Templates


app = FastAPI(
    title = "ToDo List"
)

app.mount("/static", StaticFiles(directory='todo/static'), name='static')
templates = Jinja2Templates(directory='todo/templates')

from todo.routes import home