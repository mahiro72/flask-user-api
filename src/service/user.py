from repository.user import UserRepository

class UserService():
    def __init__(self,repository:UserRepository) -> None:
        self.__repository = repository
    
    def get(self,id):
        if id == 0:
            return None,{"error":"id is invalid"}
        if id >= 20:
            return None,{"error":"id is 20 over"}
        return self.__repository.get(id),None

    def get_all(self):
        return self.__repository.get_all(),None