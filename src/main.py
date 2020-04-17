from src.user import User
from src.message import Message

def createNewUser(database):
    userName = input("Enter username for new user: ")

    # check for existing username
    if (userName in database):
        while (userName in database):
            print("That username is already taken.")
            userName = input("Enter username for new user: ")

    userPassword = input("Enter your password: ")
    confirmPassword = input("Re-enter your password: ")

    # check for password match
    if (userPassword != confirmPassword):
        while (userPassword != confirmPassword):
            print("Passwords do not match.")
            userPassword = input("Enter your password: ")
            confirmPassword = input("Re-enter your password: ")

    # setup the user's security questions
    print("You must answer two security questions.")
    answerOne = input("Question 1: What is your favorite color? \n Enter answer: ")
    answerTwo = input("Question 2: What is your favorite food? \n Enter answer: ")
    newUserSecurityQuestions = [answerOne, answerTwo]

    # put new user into database
    newUser = User(userName, userPassword, newUserSecurityQuestions)
    database[userName] = newUser

def loginUser(database):

    currUserName = input("Enter your username: ")
    if (currUserName not in database):
        while (currUserName not in database):
            print("No user with that username.")
            currUserName = input("Enter your username: ")

    currUser = database[currUserName]
    triesRemaining = 3
    userPassword = input("Enter your login password: ")
    if (userPassword != currUser.password):
        while (userPassword != currUser.password):
            if (triesRemaining == 0):
                print("Maximum tries reached to login, locking account.")
                currUser.setUserAccountStatus(True)
                return

            print(f"Incorrect password. You have {triesRemaining} tries left.")
            triesRemaining -= 1


            userPassword = input("Enter your login password: ")

    if (currUser.accountLocked is True):
        print("Your account is locked, answer the two security questions to unlock it.")
        answerOne = input("Question 1: What is your favorite color? \n Enter answer: ")
        if (currUser.securityAnswers[0] != answerOne):
            print("Incorrect answer. The account is still locked.")
            return

        answerTwo = input("Question 2: What is your favorite food? \n Enter answer: ")
        if (currUser.securityAnswers[1] != answerTwo):
            print("Incorrect answer. The account is still locked.")
            return

        else:
            print("Account unlocked.")
            currUser.accountLocked = False

    print("Successfully logged in! Select an option below:")
    print("Enter \"send message\" to send another user a message.")
    print("Enter \"read messages\" to read your own messages.")
    print("Enter \"update security questions\" to update your security questions.")
    print("Enter \"update password\" to update your password.")
    print("Enter \"logout\" to logout of your account.")
    print("Enter \"delete\" to delete your account.\n")

    userChoice = input("Enter option: ")

    # update your own password
    if (userChoice == "update password"):
        newPassword = input("Enter your new password: ")
        confirmNewPassword = input("Re-enter your new password: ")
        while (newPassword != confirmNewPassword):
            print("Passwords do not match.")
            newPassword = input("Enter your new password: ")
            confirmNewPassword = input("Re-enter your new password: ")

        print(f"Password successfully changed to: {confirmNewPassword}")
        currUser.updatePassword(newPassword)

    # update your security questions
    elif (userChoice == "update security questions"):
        currUser.clearSecurityAnswers()
        answerOne = input("Question 1: What is your favorite color? \n Enter answer: ")
        answerTwo = input("Question 2: What is your favorite food? \n Enter answer: ")
        answerList = currUser.getSecurityAnswers()
        answerList.append(answerOne)
        answerList.append(answerTwo)

    # send message to another user
    elif (userChoice == "send message"):
        userToMessage = input("Enter the username of the person you want to message:")

        while ((userToMessage not in database) or (userToMessage == currUserName)):
            print("No other user with that username.")
            userToMessage = input("Enter the username of the person you want to message:")

        userMessage = input("Enter the message to be sent:")

        receivingUser = database[userToMessage]
        outgoingMessage = Message(currUser.userName, userMessage)

        receivingUser.addMessage(outgoingMessage)
        print(f"Message successfully sent to {userToMessage}.")

    # read your own messages
    elif (userChoice == "read messages"):
        messageList = currUser.getMessageList
        for message in messageList:
            print(f"Message from {message.messageAuthor}: {message.messageText}")

    # delete your received messages
    elif (userChoice == "delete messages"):
        currUser.clearMessages()

    elif (userChoice == "logout"):
        print("Successfully logged out.")
        return

    # delete your own account
    elif (userChoice == "delete me"):
        userChoice = input("Are you sure you want to delete your account? Enter \"yes\" to confirm:")

        if (userChoice == "yes"):
            del database[currUserName]
        else:
            print("Aborting deletion of your account.")


def seedDatabase(database):

    userOneSecurityAnswerOne = "black"
    userOneSecurityAnswerTwo = "fish"
    userOneSecurityAnswers =[userOneSecurityAnswerOne, userOneSecurityAnswerTwo]
    userOne = User("ryan", "BlackHawk9", userOneSecurityAnswers)

    userTwoSecurityAnswerOne = "red"
    userTwoSecurityAnswerTwo = "apple"
    userTwoSecurityAnswers = [userTwoSecurityAnswerOne, userTwoSecurityAnswerTwo]
    userTwo = User("john", "BlackHawk9", userTwoSecurityAnswers)

    userThreeSecurityAnswerOne = "blue"
    userThreeSecurityAnswerTwo = "steak"
    userThreeSecurityAnswers = [userThreeSecurityAnswerOne, userThreeSecurityAnswerTwo]
    userThree = User("billy", "iLoveSteak", userThreeSecurityAnswers)

    userFourSecurityAnswerOne = "green"
    userFourSecurityAnswerTwo = "peas"
    userFourSecurityAnswers = [userFourSecurityAnswerOne, userFourSecurityAnswerTwo]
    userFour = User("jack", "iLovePeas", userFourSecurityAnswers)

    database["ryan"] = userOne
    database["john"] = userTwo
    database["billy"] = userThree
    database["jack"] = userFour

if __name__ == '__main__':

    # the "database" of users (will later migrate to relational database like MySQL or document based like MongoDB)
    database = {}
    seedDatabase(database)

    while True:
        print("Select one of the options listed below.")
        print("Enter \"new\" to create a new user")
        print("Enter \"login\" to login to an existing account.")
        print("Enter \"quit\" to exit the app. \n")

        inputString = input("Enter Option: ")

        # create a new user
        if inputString == "new":
            createNewUser(database)

        # login
        elif inputString == "login":
           loginUser(database)

        # quit
        elif inputString == "quit":
            exit(0)

        # test print database
        elif inputString == "test":
            for key in database:
                testUser = database[key]
                print(f"Username: {testUser.userName}. Password: {testUser.password}")
