from model.user import User

class UserRepository():
    def __init__(self,db) -> None:
        self.__db = db
    
    # userを取得し、それを返す
    def get(self,id):
        # u = self.db.hoge
        u = User(
            id=id,
            name="hoge",
            age=22,
        )
        return u
