from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from config.db.conn import CONNECT_STR


engine = create_engine(CONNECT_STR)

Base = declarative_base()

SessionClass = sessionmaker(engine)  # セッションを作るクラスを作成
session = SessionClass()

