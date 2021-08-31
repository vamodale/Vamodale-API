import os

from flask import request, g
from jwt import decode
from functools import wraps

from controller import users_controller
from error.exceptions import NotLoggedUser


def validate_login(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        user = request.headers.get('Authorization', None)

        if not user:
            raise NotLoggedUser

        user = decode(user, os.getenv('SECRET_KEY'), algorithms=[os.getenv('ALGORITHM')])
        user = users_controller.login( user['email'], user['openid'] )
        
        g.user = user

        return f(*args, **kwargs)

    return decorated_function
