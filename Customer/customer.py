from Branch.branch import Branch
from Account.account import Account
from src.save import *
from src.loan_number_generator import loan_number_generator

class Customer():
    def __init__(self, name, family, national_code, home_town, account_number: list) -> None:
        self.name = name
        self.family = family
        self.national_code = national_code
        self.home_town = home_town
        self.account_number = account_number
        self.loan_number = loan_number_generator()


    def show_details(self):
        with open("Account.txt", "r") as file:
            text = file.readlines()
            text = ''.join(text)
            print(text)


    def loan_request(self, account: Account, branch: Branch):
        if self.account_number == account.account_number:
            loan_amount = int(input("Enter the amount of loan you are requesting: "))

            if loan_amount <= branch.budget:
                account.account_amount += loan_amount
                print(f"You recieved your loan {self.name}")
            else:
                print(f"Sorry {self.name} your branch does not have this amount of loan you are requesting at the moment")
                
        else:
            print("Exception!!!")


    def deposit(self, amount, account: Account):
        if self.account_number == account.account_number:
            account.account_amount += amount
            return account.account_amount
        else:
            print("Exception!!!")


    def withdraw(self, amount, account: Account):
        if self.account_number == account.account_number:
            account.account_amount -= amount
            return account.account_amount
        else:
            print("Exception!!!")


    def open_acccount(self, branch: Branch):
        account = Account(0, f"{self.name} {self.family}")

        # with open("Branch.txt", "r") as file:
        #     text = file.readlines()
        #     text = ''.join(text)                                PUT THIS IN MENU
        #     print(text)                           


        branch.number_of_customers += 1

        save_account(account.account_owner, self.national_code, account.account_number, account.account_amount, branch.name)