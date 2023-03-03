import os


from pydantic import BaseSettings
from dotenv import load_dotenv


load_dotenv()


class Settings(BaseSettings):
    app_name = os.getenv("APP_NAME")
    db_url = os.getenv("SQLALCHEMY_DATABASE_URI")

    class Config:
        env_file: str = '../.env'



settings = Settings()