class UserNotAdmin(Exception):
    def __init__(self):
        self.msg = f"User is not the event owner."
        self.status = 401

    def __str__(self):
        return self.msg
 