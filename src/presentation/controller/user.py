from service.user import UserService
from utils.response import user
from flask import jsonify

class UserController():
    def __init__(self,service:UserService) -> None:
        self.__service = service

    def get(self,id) -> dict:
        u,err = self.__service.get(id)
        if err != None:
            return err

        uJson = user.make_response(u)
        return uJson

    def get_all(self):
        us,err = self.__service.get_all()
        if err != None:
            return err

        usJson = user.make_response_list(us)
        return jsonify({"users":usJson})
