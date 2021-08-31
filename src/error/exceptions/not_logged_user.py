class NotLoggedUser(Exception):
    def __init__(self):
        self.msg = f"User not logged in."
        self.status = 401

    def __str__(self):
        return self.msg
 