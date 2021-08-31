import traceback

from jwt import ExpiredSignatureError
from flask import Flask
from werkzeug.exceptions import HTTPException
from sqlalchemy.exc import IntegrityError

from .exceptions import *

def config_error_handler(app: Flask):
    @app.errorhandler( Exception )
    def generic_handler( err ):
        app.logger.debug(traceback.format_exc())
        app.logger.error(err)
        return { "error": str(err) }, 500

    @app.errorhandler( HTTPException )
    def generic_handler( err ):
        app.logger.debug(traceback.format_exc())
        app.logger.error(err)
        return { "error": str(err) }, err.code

    @app.errorhandler( EventAlreadyExist )
    def event_already_exist_handler(err):
        app.logger.debug(traceback.format_exc())
        app.logger.error(err)
        return { "error": err.msg }, err.status


    @app.errorhandler( UserNotFound )
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
    
    @app.errorhandler( EventNotFound )
    def event_not_found_handler(err):
        app.logger.debug(traceback.format_exc())
        app.logger.error(err)
        return { "error": err.msg }, err.status

    @app.errorhandler( NotLoggedUser )
    def event_not_found_handler(err):
        app.logger.debug(traceback.format_exc())
        app.logger.error(err)
        return { "error": err.msg }, err.status

    @app.errorhandler( UserNotAdmin )
    def event_not_found_handler(err):
        app.logger.debug(traceback.format_exc())
        app.logger.error(err)
        return { "error": err.msg }, err.status

    @app.errorhandler( ExpiredSignatureError )
    def event_not_found_handler(err):
        app.logger.debug(traceback.format_exc())
        app.logger.error(err)
        return { "error": err.msg }, 401