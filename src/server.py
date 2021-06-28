import os, json
from dotenv import load_dotenv
from flask import Flask

API_PORT = 'API_PORT'
FLASK_DEBUG = 'FLASK_DEBUG'
SERVER_CONFIG_FILENAME = 'SERVER_CONFIG_FILENAME'
FLASK_INSTANCE_RELATIVE_CONFIG = 'FLASK_INSTANCE_RELATIVE_CONFIG'

def create_app():
    load_dotenv('config/.env')

    app = Flask( __name__)

    app.config.from_file( os.getenv( SERVER_CONFIG_FILENAME ), load=json.load )

    from routes import config_routes
    config_routes(app)

    return app

if __name__ == '__main__':
    app = create_app()
    app.run( port=os.getenv( API_PORT ), 
            debug=os.getenv( FLASK_DEBUG ) )
