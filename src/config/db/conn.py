import os

DATABASE = "postgresql"
USER     = os.getenv("POSTGRES_USER")
PASSWORD = os.getenv("POSTGRES_PASSWORD")
HOST     = os.getenv("CONTAINER_NAME")
PORT     = "5432"
DB_NAME  = os.getenv("POSTGRES_DB")

CONNECT_STR = f'{DATABASE}://{USER}:{PASSWORD}@{HOST}:{PORT}/{DB_NAME}'
