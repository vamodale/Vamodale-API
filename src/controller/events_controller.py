from flask import request

from model.schema import Event
from service import events_service, users_service
from utils.decorators import verify_request_body
from error.exceptions import EventNotFound
from controller import users_controller

# @verify_request_body( Event ) TOFIX
def insert_events( body : dict ):
    events_service.validate_existence_event( body )
    event = Event.from_dict(body)
    events_service.save_event(event)
    return event

def get_all_events():
    events = events_service.get_all_events()
    return events

def get_event( event_id ):
    event = events_service.get_event_by_id( event_id )

    if not event:
        raise EventNotFound
    return event

def get_users_event( event_id ):
    event = get_event( event_id )
    users = events_service.get_users_event( event )

    return users

def insert_user_event( event_id, user_id ):
    event = get_event( event_id )
    user = users_controller.get_user( user_id )

    return event
