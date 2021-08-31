from flask import request

from model.schema import Event
from utils.restease import get_city_from_cep
from service import events_service, users_service
from utils.decorators import verify_request_body
from error.exceptions import EventNotFound, UserNotAdmin
from controller import users_controller

# @verify_request_body( Event ) TOFIX
def insert_events( body : dict ):
    events_service.validate_existence_event( body )
    body['cidade'] = get_city_from_cep( body['cep'] )
    event = Event.from_dict(body)
    events_service.save_event(event)
    return event

def get_all_events( user ):
    events = events_service.get_all_events( user )
    return events

def get_event( event_id ) -> Event:
    event = events_service.get_event_by_id( event_id )

    if not event:
        raise EventNotFound
    return event

def get_users_event( event_id ):
    event = get_event( event_id )
    users = events_service.get_users_event( event )

    return users

def insert_user_event( event_id, user ):
    event = get_event( event_id )
    events_service.insert_user_event( event, user )

    return event

def edit_event( event_id, new_event, user ):
    event = get_event(event_id)

    if event.id_criador != user.id:
        raise UserNotAdmin
    
    event = events_service.edit_event( event_id, new_event )
