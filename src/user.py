class User:

    username = None
    password = None

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def updatePassword(self, newPassword):
        self.password = newPassword