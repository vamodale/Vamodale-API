import os

from flask import request
from jwt import encode
from functools import wraps

from error.exceptions import NotLoggedUser
import datetime

def generate_token(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        user = f(*args, **kwargs)

        email = user.email
        openid = user.openid

        token = encode({
            "email": email,
            "openid": openid,
            "exp": datetime.datetime.utcnow() + datetime.timedelta(days=7) 
        }, os.getenv('SECRET_KEY'), algorithm=os.getenv('ALGORITHM'))

        return {"Authorization": token}, 200
    return decorated_function
