from flask import Blueprint, request, jsonify, g
from controller import events_controller
from model.dto import EventDTO, UserDTO

from utils.decorators import validate_login

events_router = Blueprint('events', __name__, url_prefix='/events')

@events_router.post('/')
@validate_login
def post_events():
    a = request.json
    a['id_criador'] = g.user.id
    event = events_controller.insert_events( request.json )
    return EventDTO( event ).to_dict(), 200

@events_router.get('/')
@validate_login
def get_all_events():
    events = events_controller.get_all_events( g.user )
    events = [ EventDTO( event ).to_dict() for event in events ]
    return jsonify(events), 200

@events_router.get('/<event_id>')
def get_event( event_id ):
    event = events_controller.get_event( event_id )
    return EventDTO( event ).to_dict(), 200

#TODO
@events_router.put('/<event_id>')
@validate_login
def edit_event( event_id ):
    event = events_controller.edit_event( event_id, request.json, user )
    return EventDTO( event ).to_dict(), 200

@events_router.post('/<event_id>/users')
@validate_login
def insert_user( event_id ):
    event = events_controller.insert_user_event( event_id, g.user )
    return {"msg": "Successfully user added"}, 200
    
@events_router.get('/<event_id>/users')
def get_users( event_id ):
    users = events_controller.get_users_event( event_id )
    users = [ UserDTO(user).to_dict() for user in users ]
    return jsonify(users), 200
