from src.user import User

while (True):
    print("Select one of the options listed below.")
    print("Enter \"NEW\" to create a new user")
    print("Enter \"LOGIN\" to login to an existing account.")
    print("Enter \"UPDATE\" to update existing user's password.")
    print("Enter \"QUIT\" to exit the app. \n")

    inputString = input("Enter Option:")

    if inputString == "NEW":

        userName = input("Please enter username for new user:")
        userPassword = input("Please enter password:")
        confirmPassword = input("Please re-enter password:")

        if (userPassword != confirmPassword):
            while (userPassword != confirmPassword):
                print("Passwords do not match.")
                userPassword = input("Please enter password:")
                confirmPassword = input("Please re-enter password:")

        newUser = User(userName, userPassword)

