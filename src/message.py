from datetime import datetime

class Message:

    messageAuthor = None
    messageText = None
    messageTime = None

    def __init__(self, messageAuthor, messageText):
        self.messageAuthor = messageAuthor
        self.messageText = messageText
        self.messageTime  = datetime.now()

    def getMessageAuthor(self):
        return self.messageAuthor

    def setMessageAuthor(self, messageAuthor):
        self.messageAuthor = messageAuthor

    def getMessageText(self):
        return self.messageText

    def setMessageText(self, messageText):
        self.messageText = messageText

    def printMessageTime(self):
        print(self.messageTime.strftime("%d/%m/%Y %H:%M:%S"))