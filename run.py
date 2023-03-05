# Данный модуль предназначен для запуска приложения
import os

import uvicorn
from todo.main import app



if __name__ == "__main__":
    uvicorn.run("run:app", host="localhost", port=os.getenv("PORT", default=5000), log_level="info")