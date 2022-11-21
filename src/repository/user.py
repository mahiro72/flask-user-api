from model.user import User
from sqlalchemy.schema import Column
from sqlalchemy.types import Integer, String
from config.db.db import Base

class UserDto(Base):
    __tablename__ = "users"

    id   = Column(Integer, primary_key=True)
    name = Column(String(255))
    age  = Column(Integer)


class UserRepository():
    def __init__(self,session) -> None:
        self.__session = session

    # userを取得し、それを返す
    def get(self,id):
        dto = self.__session.query(UserDto).\
        filter(UserDto.id==id).\
        limit(1).\
        one()

        return dto_to_user(dto)

    # すべてのユーザーを取得する
    def get_all(self):
        dtos = self.__session.query(UserDto).\
        all()

        return dtos_to_users(dtos)

def dto_to_user(dto:UserDto):
    return User(
        id=dto.id,
        name=dto.name,
        age=dto.age
    )

def dtos_to_users(dtos:list):
    users = []
    for dto in dtos:
        users.append(dto_to_user(dto))
    return users

