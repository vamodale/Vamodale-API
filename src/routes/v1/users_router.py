from src.model.dto.users_dto import UserDTO
from flask import Blueprint, request

from controller import users_controller

users_router = Blueprint('users', __name__, url_prefix='/users')

@users_router.post('/')
def post_user():
    return users_controller.insert_user( request.json )

@users_router.get('/')
def get_users():
    users = users_controller.get_all_users()
    users = [UserDTO(user).to_dict() for user in users]
    users = {"usuarios": users}
    return users, 200


@users_router.get('/<user_id>')
def get_user_by_id(user_id):
    user = users_controller.get_user(user_id)
    return UserDTO(user).to_dict(), 200
