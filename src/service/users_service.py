from model.schema import Usuario

def save_user( user : Usuario ):
    return user.save()

def get_all_users():
    users = Usuario.search()
    return users

def get_user_by_id( user_id ):
    user = Usuario.get_by_id( user_id )
    return user

def get_events_user( user : Usuario ):
    return user.get_events()

def get_user_by_email_and_openid( email, openid ):
    user = Usuario.login( email, openid )
    return user
