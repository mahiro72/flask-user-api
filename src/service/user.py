from repository.user import UserRepository

class UserService():
    def __init__(self,repository:UserRepository) -> None:
        self.__repository = repository
    
    def get(self,id):
        return self.__repository.get(id)

