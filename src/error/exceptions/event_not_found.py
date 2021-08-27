class EventNotFound(Exception):
    def __init__(self):
        self.msg = f"Event not Found."
        self.status = 400

    def __str__(self):
        return self.msg
 