from sqlalchemy.orm.session import Session
from sqlalchemy.orm import sessionmaker

from config.db.db import engine


session_class   = sessionmaker(engine)
session:Session = session_class()