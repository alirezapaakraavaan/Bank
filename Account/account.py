from src.account_number_generator import account_number_generator

class Account():
    def __init__(self, account_amount=None, account_owner=None):
        self.account_number = account_number_generator()
        self.account_amount = account_amount
        self.account_owner = account_owner


    def show_details(self):
        with open("Account.txt", "r") as file:
            text = file.readlines()
            text = ''.join(text)
            print(text)