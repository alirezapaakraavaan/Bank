from src.check_password_for_admin import check_password_for_admin

def menu():
    role = input("\n\nWelcome to the BANK\n\nIf you are a user please enter number 1 and if you are admin enter 2 to enter: ")

    if role == "1":
        print("Hi user")
    else:
        password = input("Enter the password: \n\n")
        check_password_for_admin(password)