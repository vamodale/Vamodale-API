from flask import request

from model.schema import Usuario
from model.dto import UserDTO
from service import users_service
from utils.decorators import verify_request_body

@verify_request_body( Usuario )
def insert_user( body : dict ):
    #TODO Inserir esportes do usuario 
    user = Usuario.from_dict(body)
    users_service.save_user(user)
    return UserDTO( user ).to_dict(), 200

def get_all_users():
    users = users_service.get_all_users()
    return users