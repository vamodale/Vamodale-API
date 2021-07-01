from functools import wraps

from database import BaseModel
from error.exceptions import MissingInformationException
from flask import request

def verify_request_body( cls : BaseModel ):
    def inner_function( func ):
        @wraps(func)
        def wrapper( *args, **kwargs ):
            body = request.json
            for event_param, column in ( items for items in vars(cls).items() if not items[0].startswith('_') and not callable(items[1]) ):
                if event_param in ("id", "created_at") or column.nullable:
                    continue
                if body.get( event_param ) is None:
                    raise MissingInformationException( event_param )
            return func( *args, **kwargs )
        return wrapper
    return inner_function