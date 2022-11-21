from flask import Blueprint
from presentation.controller.user import UserController
from repository.user import UserRepository
from service.user import UserService
from config.db.db import session

# api
api = Blueprint('user',__name__)

# private variable
__r = UserRepository(session)
__s = UserService(__r)
__c = UserController(__s)

@api.route("/user/<int:id>")
def get(id):return __c.get(id)

@api.route("/user/all")
def get_all():return __c.get_all()
