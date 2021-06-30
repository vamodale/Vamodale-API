from model.schema import Event

ALREADY_EXISTS = 1

def save_event( event : Event ):
    return event.save()

def validate_existence_event( body : dict ):
    events = Event.search( **body )
    if len(events) >= ALREADY_EXISTS:
        raise Exception("ai é foda")
