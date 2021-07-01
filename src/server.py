import os, json
from dotenv import load_dotenv
from flask import Flask
from waitress import serve

API_PORT = 'API_PORT'
FLASK_DEBUG = 'FLASK_DEBUG'
SERVER_CONFIG_FILENAME = 'SERVER_CONFIG_FILENAME'
FLASK_INSTANCE_RELATIVE_CONFIG = 'FLASK_INSTANCE_RELATIVE_CONFIG'
FLASK_ENV = 'FLASK_ENV'

def create_app():
    load_dotenv('config/.env')

    app = Flask( __name__)

    app.config.from_file( os.getenv( SERVER_CONFIG_FILENAME ), load=json.load )

    from routes import config_routes
    config_routes(app)

    from error import config_error_handler
    config_error_handler(app)

    return app

if __name__ == '__main__':
    app = create_app()
    # serve(app, listen='*:3333')
    if os.getenv( FLASK_ENV ) == "development":
        app.run( port=os.getenv( API_PORT ), 
                debug=os.getenv( FLASK_DEBUG ) )
    else:
        app.run( port=os.getenv("PORT") )