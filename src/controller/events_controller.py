from flask import request

from model.schema import Event
from model.dto import EventDTO
from service import events_service
from utils.decorators import verify_request_body

@verify_request_body( Event )
def insert_events( body : dict ):
    events_service.validate_existence_event( body )
    event = Event.from_dict(body)
    events_service.save_event(event)
    return EventDTO( event ).to_dict(), 200