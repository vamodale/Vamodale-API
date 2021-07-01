from model.schema import Event
from error.exceptions import EventAlreadyExist

ALREADY_EXISTS = 1

def save_event( event : Event ):
    return event.save()

def validate_existence_event( body : dict ):
    body['num_vagas'] = body.get('num_vagas', None)
    events = Event.search( **body )
    if len(events) >= ALREADY_EXISTS:
        raise EventAlreadyExist
