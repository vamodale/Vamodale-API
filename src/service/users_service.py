from model.schema import Usuario

def save_user( user : Usuario ):
    return user.save()

def get_user_by_id( user_id ):
    user = Usuario.get_by_id( user_id )
    return user
