from flask import Blueprint

v1_router = Blueprint('v1', __name__, url_prefix='/v1')

from .events_router import events_router
v1_router.register_blueprint( events_router )

from .users_router import users_router
v1_router.register_blueprint( users_router )
