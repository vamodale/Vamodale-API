from flask import request

from model.schema import Usuario
from error.exceptions import UserNotFound
from model.dto import UserDTO
from service import users_service
from utils.decorators import verify_request_body

# @verify_request_body( Usuario ) TOFIX
def insert_user( body : dict ):
    user = Usuario.from_dict(body)

    users_service.save_user(user)
    return user

def get_all_users():
    users = users_service.get_all_users()
    return users
  
def get_user( user_id ):
    user = users_service.get_user_by_id( user_id )

    if not user:
        raise UserNotFound
    return user

def login( email, openid ):
    user = users_service.get_user_by_email_and_openid( email, openid )

    if not user:
        raise UserNotFound
    return user

def get_events_user( user_id ):
    user = get_user( user_id )
    events = users_service.get_events_user( user )

    return events
