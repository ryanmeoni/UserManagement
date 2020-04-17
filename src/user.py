class User:

    username = None
    password = None
    accountLocked = None
    securityAnswers = []
    messageList = []

    def __init__(self, username, password, securityAnswers):
        self.username = username
        self.password = password
        self.securityAnswers = securityAnswers
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

    def clearSecurityAnswers(self):
        self.securityQuestions.clear()

    def getSecurityAnswers(self):
        return self.securityAnswers
