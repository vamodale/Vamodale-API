class MissingInformationException(Exception):
    def __init__(self, msg):
        self.msg = f"Missing information {msg}"
        self.status = 400

    def __str__(self):
        return self.msg
 