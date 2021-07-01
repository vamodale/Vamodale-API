import traceback

from flask import Flask
from sqlalchemy.exc import IntegrityError

from .exceptions import *

def config_error_handler(app: Flask):
    @app.errorhandler( Exception )
    def generic_handler( err ):
        app.logger.debug(traceback.format_exc())
        app.logger.error(err)
        return { "error": str(err) }, 500

    @app.errorhandler( EventAlreadyExist )
    def event_already_exist_handler(err):
        app.logger.debug(traceback.format_exc())
        app.logger.error(err)
        return { "error": err.msg }, err.status

    @app.errorhandler( MissingInformationException )
    def missing_information_handler(err):
        app.logger.debug(traceback.format_exc())
        app.logger.error(err)
        return { "error": err.msg }, err.status

    @app.errorhandler( IntegrityError )
    def integrity_error_handler(err):
        app.logger.debug(traceback.format_exc())
        app.logger.error(err)
        return { "error": "Lack of integrity on insert's values" }, 400
