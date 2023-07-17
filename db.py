import os
from dotenv import load_dotenv
from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise

load_dotenv('db.env')
database = os.getenv('POSTGRES_DB')
db_user = os.getenv('POSTGRES_USER')
db_password = os.getenv('POSTGRES_PASSWORD')
db_host = os.getenv('PG_HOST')
db_port = os.getenv('POSTGRES_PORT')


# Загрузка БД (load db)
def load_db(app: FastAPI):
    register_tortoise(
        app,
        db_url=f"postgres://{db_user}:{db_password}@{db_host}:{db_port}/{database}",
        modules={"models": ["models"]},
        generate_schemas=True,
        add_exception_handlers=True,
    )
