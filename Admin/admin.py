from Bank.bank import Bank
from src.save import *
from Branch.branch import Branch
from Account.account import Account
from src.get_branch_details import *

class Admin():
    def __init__(self, name, family, national_code, password):
        self.name = name
        self.family = family
        self.national_code = national_code
        self.password = password
        save_password(password)


    def show_data(self, bank: Bank, branch: Branch, account: Account):
        bank.show_details()
        branch.show_details()
        account.show_details()


    def create_bank(self):
        name = input("Enter the bank's name: ")
        bank_id = input("Enter an id for the bank: ")
        bank = Bank(name, bank_id)
        save_bank(bank.name, bank.bank_id)


    def create_branch(self):
        name = input("Enter the branch's name: ")
        bank_id = input("Enter the id of this branch's bank: ")
        city_name = input("Enter the name of the city this branch is located at: ")
        branch = Branch(name, bank_id, 0, city_name)
        save_branch(branch.name, branch.bank_id, branch.number_of_customers, branch.budget, branch.city_name)


    def determine_budget(self):
        branch_name = input("Please enter the name of branch you want to determine it's budget: ")
        budget = int(input("Enter the budget of this branch: "))
        words = get_branch_details(branch_name)
        new_budget = 0
        if words[1] == branch_name:
            old_budget = words[3]
            old_budget = int(old_budget)
            new_budget = old_budget + budget
        edit_branch_file(branch_name)
        save_branch(words[1], words[2], words[3], new_budget, words[5])
        


    def change_password(self):
        current_password = input("Enter your current password: \n")
        if current_password == self.password:
            new_password = input("Enter your new password: \n")
            self.password = new_password

            with open("admin_password.txt", "w") as file:
                file.write(new_password)

        else:
            print("This is not your current password!")