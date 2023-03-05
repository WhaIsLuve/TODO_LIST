# Данный модуль создает модель БД

from todo.database.base import Base, engine
from sqlalchemy import Column, Integer, String, Boolean


class ToDo(Base):
    __tablename__ = 'todo'

    id = Column(Integer, primary_key=True, index=True)
    tittle = Column(String, nullable=False)
    is_complete = Column(Boolean, default=False)

Base.metadata.create_all(bind=engine)