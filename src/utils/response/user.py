from model.user import User

def make_response(user:User):
    return {
        "id":user.id,
        "name":user.name,
        "age":user.age,
    }
