from flask import Blueprint, request
from controller import events_controller
from model.dto import EventDTO


events_router = Blueprint('events', __name__, url_prefix='/events')

@events_router.post('/')
def post_events():
    event = events_controller.insert_events( request.json )
    return evento, 200

@events_router.get('/')
def get_all_events():
    events = events_controller.get_all_events()
    events = [ EventDTO( event ).to_dict() for event in events ]
    events = { "eventos": events }
    return events, 200

@events_router.get('/<event_id>')
def get_events( event_id ):
    event = events_controller.get_events( event_id )
    return EventDTO( event ).to_dict(), 200

@events_router.post('/<event_id>/users/<user_id>')
def insert_user( event_id, user_id ):
    event = events_controller.insert_user_event( event_id, user_id )
    return {"msg": "Successfully user added"}, 200
