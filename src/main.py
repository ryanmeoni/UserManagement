from src.user import User

# the "database" of users (will later migrate to relational database like MySQL or document based like MongoDB)
database = {}

while (True):
    print("Select one of the options listed below.")
    print("Enter \"new\" to create a new user")
    print("Enter \"login\" to login to an existing account.")
    print("Enter \"quit\" to exit the app. \n")

    inputString = input("Enter Option: ")

    # create a new user
    if inputString == "new":
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

    # login
    elif inputString == "login":
        userName = input("Enter your username: ")
        if (userName not in database):
            while(userName not in database):
                print("No user with that username.")
                userName = input("Enter your username: ")

        currUser = database[userName]
        userPassword = input("Enter your login password: ")
        if (userPassword != currUser.password):
            while (userPassword != currUser.password):
                print("Incorrect password.")
                userPassword = input("Enter your login password: ")

        print("Successfully logged in! Select an option below:")
        print("Enter \"update\" to update password.")

        userChoice = input("Enter option: ")

        if (userChoice == "update"):
            newPassword = input("Enter your new password: ")
            confirmNewPassword = input("Re-enter your new password: ")
            while (newPassword != confirmNewPassword):
                print("Passwords do not match.")
                newPassword = input("Enter your new password: ")
                confirmNewPassword = input("Re-enter your new password: ")

            currUser.updatePassword(newPassword)

            
