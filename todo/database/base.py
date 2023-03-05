# Данный модуль предназначен для создания движка БД и локальной сессии
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker, Session
from todo.config import settings


BASE_DIR = os.path.dirname(os.path.abspath(__name__))
db_path = os.path.join(BASE_DIR, 'todo', 'database', 'DB')
if not os.path.exists(db_path):
    os.makedirs(db_path)


Base = declarative_base()


def get_db() -> Session:
    """
    Данная функция создает локальную сессию  у БД и закрывает ее после обращения
    """
    db_session_local = SessionLocal()
    try:
        yield db_session_local
    finally:
        db_session_local.close()



engine = create_engine(settings.db_url, connect_args={'check_same_thread': False}, echo=True)


SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)