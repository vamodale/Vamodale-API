from flask import Blueprint, request
from controller import events_controller

events_router = Blueprint('events', __name__, url_prefix='/events')

@events_router.post('/')
def teste():
    return events_controller.insert_events( request.json )
