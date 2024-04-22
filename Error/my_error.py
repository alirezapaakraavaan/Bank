class MyError(Exception):

    def __init__(self, role, msg="Wronge number"):
        self.message = msg
        self.role = role
        super().__init__(self.message)

    def __repr__(self):
        return f"{self.role} is not valid!"