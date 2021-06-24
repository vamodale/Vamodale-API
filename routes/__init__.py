from flask import Blueprint, Flask

events = Blueprint('/', __name__)

@events.get('/')
def teste():
    return 'aloooooo'

def config_routes( app : Flask ):
    app.register_blueprint( events )
