from flask import Blueprint, Flask

def config_routes(app : Flask):
    from routes.v1 import v1_router
    app.register_blueprint(v1_router)
