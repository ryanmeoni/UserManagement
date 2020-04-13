class User:

    username = None
    password = None
    messageList = []

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def updatePassword(self, newPassword):
        self.password = newPassword

    def addMessage(self, message):
        self.messageList.append(message)

    def clearMessages(self):
        self.messageList.clear()
