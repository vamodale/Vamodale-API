from flask import request

from model.schema import Event
from service import events_service
from utils.decorators import verify_request_body

@verify_request_body( Event )
def insert_events( body : dict ):
    events_service.validate_existence_event( body )
    event = Event.from_dict(body)
    events_service.save_event(event)
    #TODO
    # ERROR HANDLER AND ERRORS RESPONSE
    # CREATE ERROR TO EXIST EVENT AND DATABASES ERROR
    # RETURN EVENT DTO
    return event.to_dict(), 200