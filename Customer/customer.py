from Account.account import Account
from src.save import *
from src.loan_number_generator import loan_number_generator
from src.account_number_generator import account_number_generator
from src.get_user_branch_name import get_user_branch_name
from src.increase_branch_customer_count import increase_branch_customer_count
import re


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


    @staticmethod
    def loan_request(self: str, account_number, customer_branch):
        self = self.split()
        loan_amount = int(input("Enter the amount of loan you are requesting: "))

        with open("Branch.txt", "r") as file:
            for text in file.readlines():
                if customer_branch in text:
                    branch_budget = increase_branch_customer_count(customer_branch, 2)
                    branch_budget = int(branch_budget)
                    break
                else:
                    print("Branch not found!")

        if loan_amount <= branch_budget:
            with open("Account.txt", "r") as file:
                all_text = file.readlines()

            with open("Account.txt", "w") as file:
                for i, line in enumerate(all_text):
                    if account_number in line:
                        result = line.split()
                        customer_budget = result[-7]
                        customer_budget = int(customer_budget)
                        customer_budget += loan_amount
                        customer_budget = str(customer_budget)
                        text_list = re.findall(r'\S+|\s', line)
                        text_list[-14] = customer_budget
                        all_text[i] = ''.join(text_list)

            with open("Account.txt", "w") as file:
                file.writelines(all_text)


            print(f"You recieved your loan")
        else:
            print(f"Sorry your branch does not have this amount of loan you are requesting at the moment")


    @staticmethod
    def deposit(self, amount, account_number, account_amount):
        if self.account_number == account_number:
            account_amount += amount
            return account_amount
        else:
            print("Exception!!!")


    @staticmethod
    def withdraw(self, amount, account_number, account_amount):
        if self.account_number == account_number:
            account_amount -= amount
            return account_amount
        else:
            print("Exception!!!")


    def open_acccount(self, branch_name):
        account = Account(0, f"{self.name} {self.family}")

        user_branch = get_user_branch_name(branch_name)

        increase_branch_customer_count(branch_name, 1) 

        save_account(account.account_owner, self.national_code, account.account_number, account.account_amount, user_branch)