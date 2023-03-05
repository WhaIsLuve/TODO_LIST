# Данный модуль предзначен для HTTP и БД запросам
from todo.database.base import get_db
from todo.models import ToDo
from todo.config import settings
from todo.main import app, templates
from sqlalchemy.orm import Session
from fastapi import Depends, Form, Request
from starlette.responses import RedirectResponse
from starlette.templating import _TemplateResponse
from starlette.status import HTTP_303_SEE_OTHER, HTTP_302_FOUND


@app.get('/')
def home(request: Request, db_session: Session = Depends(get_db)) -> _TemplateResponse:
    """
    Данная функция развертывает frontend часть и показывает все ToDO
    """
    todo = db_session.query(ToDo).all()
    return templates.TemplateResponse('todo/index.html',
                                      {'request': request,
                                       'app_name': settings.app_name,
                                       'todo_list': todo}
                                      )


@app.post("/add")
def add(title: str = Form(...), db_session: Session = Depends(get_db)) -> RedirectResponse:
    """
    Данная функция принимает строку и добавляет ее на главную страницу и в БД
    """
    new_todo = ToDo(tittle=title)
    db_session.add(new_todo)
    db_session.commit()

    url = app.url_path_for("home")
    return RedirectResponse(url=url, status_code=HTTP_303_SEE_OTHER)


@app.get("/update/{todo_id}")
def update(todo_id: int, db_session: Session = Depends(get_db)) -> RedirectResponse:
    """
    Данная функция принимает id ToDo и изменяет его статус в БД и на главной странице
    """
    todo = db_session.query(ToDo).filter(ToDo.id == todo_id).first()
    todo.is_complete = not todo.is_complete
    db_session.commit()

    url = app.url_path_for('home')

    return RedirectResponse(url, status_code=HTTP_302_FOUND)


@app.get('/delete/{todo_id}')
def delete(todo_id: int, db_session: Session = Depends(get_db)) -> RedirectResponse:
    """
    Данная функция принимает id ToDo и удаляет его в БД и на главной странице
    """
    todo = db_session.query(ToDo).filter(ToDo.id == todo_id).first()
    db_session.delete(todo)
    db_session.commit()


    url = app.url_path_for('home')

    return RedirectResponse(url, status_code=HTTP_302_FOUND)