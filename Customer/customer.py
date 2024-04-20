from Branch.branch import Branch
from Account.account import Account
from src.save import *
from src.loan_number_generator import loan_number_generator
from src.account_number_generator import account_number_generator
from src.get_user_branch_name import get_user_branch_name


class Customer():
    def __init__(self, name, family, national_code, home_town) -> None:
        self.name = name
        self.family = family
        self.national_code = national_code
        self.home_town = home_town
        self.account_number = account_number_generator()
        self.loan_number = loan_number_generator()
        self.account_amount = 0
        self.customer_branch = ""


    def show_details(self, national_code=None):
        with open("Account.txt", "r") as file:
            for text in file:
                if national_code in text:
                    print(text.strip())
                elif national_code==None:
                    text = file.readlines()
                    text = ''.join(text)
                    print(text)
                else:
                    print("User not found!")
            print(text)


    def loan_request(self, account_number, account_amount, customer_branch):
        if self.account_number == account_number:
            loan_amount = int(input("Enter the amount of loan you are requesting: "))

            with open("Branch.txt", "r") as file:
                for text in file:
                    if customer_branch in text:
                        text = text.strip()
                        branch_budget = text.split()[3]
                    else:
                        print("Branch not found!")

            if loan_amount <= branch_budget:
                account_amount += loan_amount
                print(f"You recieved your loan {self.name}")
            else:
                print(f"Sorry {self.name} your branch does not have this amount of loan you are requesting at the moment")
                
        else:
            print("Exception!!!")


    def deposit(self, amount, account_number, account_amount):
        if self.account_number == account_number:
            account_amount += amount
            return account_amount
        else:
            print("Exception!!!")


    def withdraw(self, amount, account_number, account_amount):
        if self.account_number == account_number:
            account_amount -= amount
            return account_amount
        else:
            print("Exception!!!")


    def open_acccount(self, branch_name):
        account = Account(0, f"{self.name} {self.family}")

        user_branch = get_user_branch_name(branch_name)

        save_account(account.account_owner, self.national_code, account.account_number, account.account_amount, user_branch)