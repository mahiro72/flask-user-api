from model.user import User

def make_response(user:User):
    return {
        "id"   : user.id,
        "name" : user.name,
        "age"  : user.age,
    }

def make_response_list(users:list):
    usJson = []
    for u in users:
        usJson.append(make_response(u))
    return usJson
