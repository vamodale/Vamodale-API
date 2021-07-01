class EventAlreadyExist(Exception):
    def __init__(self):
        self.msg = f"Event with this informations already exist."
        self.status = 400

    def __str__(self):
        return self.msg
 