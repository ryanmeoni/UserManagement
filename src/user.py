class User:

    username = None
    password = None
    accountLocked = None
    securityQuestions = []
    messageList = []

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.accountLocked = False

    def setPassword(self, newPassword):
        self.password = newPassword

    def getPassword(self):
        return self.password

    def addMessage(self, message):
        self.messageList.append(message)

    def clearMessages(self):
        self.messageList.clear()

    def getMessages(self):
        return self.messageList

    def getUserAccountStatus(self):
        return self.accountLocked

    def setUserAccountStatus(self, accountLockedStatus):
        self.accountLocked = accountLockedStatus

    def clearSecurityQuestions(self):
        self.securityQuestions.clear()

    def getSecurityQuestions(self):
        return self.securityQuestions
