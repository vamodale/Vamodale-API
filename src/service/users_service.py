from model.schema import Usuario

def save_user( user : Usuario ):
    return user.save()
