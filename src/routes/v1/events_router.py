from flask import Blueprint, request, jsonify
from controller import events_controller
from model.dto import EventDTO, UserDTO


events_router = Blueprint('events', __name__, url_prefix='/events')

@events_router.post('/')
def post_events():
    event = events_controller.insert_events( request.json )
    return EventDTO( event ).to_dict(), 200

@events_router.get('/')
def get_all_events():
    events = events_controller.get_all_events()
    events = [ EventDTO( event ).to_dict() for event in events ]
    return jsonify(events), 200

@events_router.get('/<event_id>')
def get_event( event_id ):
    event = events_controller.get_event( event_id )
    return EventDTO( event ).to_dict(), 200

@events_router.post('/<event_id>/users/<user_id>')
def insert_user( event_id, user_id ):
    event = events_controller.insert_user_event( event_id, user_id )
    return {"msg": "Successfully user added"}, 200
    
@events_router.get('/<event_id>/users')
def get_users( event_id ):
    users = events_controller.get_users_event( event_id )
    users = [ UserDTO(user).to_dict() for user in users ]
    return jsonify(users), 200
