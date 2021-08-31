from model.dto import UserDTO, EventDTO
from flask import Blueprint, request, jsonify, g

from controller import users_controller
from utils.decorators import generate_token
from utils.decorators import validate_login

users_router = Blueprint('users', __name__, url_prefix='/users')

@users_router.post('/')
@generate_token
def post_user():
    user = users_controller.insert_user( request.json )
    return user

@users_router.get('/')
def get_users():
    users = users_controller.get_all_users()
    users = [UserDTO(user).to_dict() for user in users]
    return jsonify(users), 200

@users_router.get('/<user_id>')
def get_user_by_id(user_id):
    user = users_controller.get_user(user_id)
    return UserDTO(user).to_dict(), 200

@users_router.get('/profile')
@validate_login
def get_profile():
    user = g.user
    return UserDTO(user).to_dict(), 200

@users_router.get('/events')
@validate_login
def get_user_events():
    events = users_controller.get_events_user( g.user )
    events = [ EventDTO(user).to_dict() for user in events ]
    return jsonify(events), 200
