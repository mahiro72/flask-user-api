from service.user import UserService
from utils.response import user

class UserController():
    def __init__(self,service:UserService) -> None:
        self.__service = service

    def get(self,id) -> dict:
        u = self.__service.get(id)
        uJson = user.make_response(u)
        return uJson
