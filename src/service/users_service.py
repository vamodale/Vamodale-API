from model.schema import Usuario, Event

def save_user( user : Usuario ):
    return user.save()

def get_all_users():
    users = Event.search()
    return users

# TODO get_user_by_id method