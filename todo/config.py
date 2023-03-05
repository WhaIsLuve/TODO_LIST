# Данный модуль предназначен для обращение к .env

import os


from pydantic import BaseSettings
from dotenv import load_dotenv


load_dotenv()


class Settings(BaseSettings):
    """
    Класс для обращениям константам из .env
    """
    app_name = os.getenv("APP_NAME")
    db_url = os.getenv("SQLALCHEMY_DATABASE_URI")




settings = Settings()