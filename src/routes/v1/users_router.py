from flask import Blueprint, request

from controller import users_controller

users_router = Blueprint('users', __name__, url_prefix='/users')

@users_router.post('/')
def post_user():
    return users_controller.insert_user( request.json )
