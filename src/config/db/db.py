from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.engine import Engine

from config.db.conn import get_conn


Base           = declarative_base()
engine:Engine  = create_engine(get_conn())
