def check_password_for_admin(password):
    with open("admin_password.txt", "r") as file:
        text = file.readlines()
        text = ''.join(text)

    if password == text:
        return "Succeed\nHi admin"
    else:
        return "Failed!"