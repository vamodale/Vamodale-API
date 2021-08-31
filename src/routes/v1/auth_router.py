from model.dto import UserDTO, EventDTO
from flask import Blueprint, request, jsonify

from controller import users_controller
from utils.decorators  import generate_token

users_router = Blueprint('auth', __name__, url_prefix='/auth')

@users_router.get('/login')
@generate_token
def login():
    user = users_controller.login( request.json['email'], request.json['openid'] )
