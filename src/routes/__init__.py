from flask import Blueprint, Flask

v1_router = Blueprint('v1', __name__, url_prefix='/v1')

from .events_router import events_router
v1_router.register_blueprint( events_router )


def config_routes(app : Flask):
    app.register_blueprint(v1_router)
