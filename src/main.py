from src.user import User

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

    # put new user into database
    newUser = User(userName, userPassword)
    database[userName] = newUser

def loginUser(database):
    currUserName = input("Enter your username: ")
    if (currUserName not in database):
        while (currUserName not in database):
            print("No user with that username.")
            currUserName = input("Enter your username: ")

    currUser = database[currUserName]
    userPassword = input("Enter your login password: ")
    if (userPassword != currUser.password):
        while (userPassword != currUser.password):
            print("Incorrect password.")
            userPassword = input("Enter your login password: ")

    print("Successfully logged in! Select an option below:")
    print("Enter \"update\" to update your password.")
    print("Enter \"send message\" to send another user a message.")
    print("Enter \"read messages\" to read your own messages.")
    print("Enter \"delete\" to delete your account.\n")

    userChoice = input("Enter option: ")

    # update your own password
    if (userChoice == "update"):
        newPassword = input("Enter your new password: ")
        confirmNewPassword = input("Re-enter your new password: ")
        while (newPassword != confirmNewPassword):
            print("Passwords do not match.")
            newPassword = input("Enter your new password: ")
            confirmNewPassword = input("Re-enter your new password: ")

        print(f"Password successfully changed to: {confirmNewPassword}")
        currUser.updatePassword(newPassword)

    # send message to another user
    elif (userChoice == "send message"):
        userToMessage = input("Enter the username of the person you want to message:")

        while ((userToMessage not in database) or (userToMessage == currUserName)):
            print("No other user with that username.")
            userToMessage = input("Enter the username of the person you want to message:")

        userMessage = input("Enter the message to be sent:")

        recievingUser = database[userToMessage]
        recievingUser.addMessage((currUserName, userMessage))
        print(f"Message successfully sent to {userToMessage}.")

    # read your own messages
    elif (userChoice == "read messages"):
        messageList = currUser.messageList
        for message in messageList:
            print(f"Message from {message[0]}: {message[1]}")

    # delete your own account
    elif (userChoice == "delete me"):
        userChoice = input("Are you sure you want to delete your account? Enter yes to confirm:")

        if (userChoice == "yes"):
            del database[currUserName]
        else:
            print("Aborting deletion of your account.")


if __name__ == '__main__':

    # the "database" of users (will later migrate to relational database like MySQL or document based like MongoDB)
    database = {}

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
                print(testUser.password)
