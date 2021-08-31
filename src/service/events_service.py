from model.schema import Event, Usuario
from error.exceptions import EventAlreadyExist

ALREADY_EXISTS = 1

def save_event( event : Event ):
    return event.save()

def validate_existence_event( body : dict ):
    body['num_vagas'] = body.get('num_vagas', None)
    events = Event.search( **body )
    if len(events) >= ALREADY_EXISTS:
        raise EventAlreadyExist

def get_event_by_id( event_id ):
    event = Event.get_by_id( event_id )
    return event

def get_all_events( user ):
    events = Event.get_events_by_city( user.cidade)
    return events

def insert_user_event( event : Event, user : Usuario ):
    return event.add_jogador( user )

def get_users_event( event : Event ):
    return event.get_jogadores()

def edit_event( event : Event, new_event : dict ):
    pass
