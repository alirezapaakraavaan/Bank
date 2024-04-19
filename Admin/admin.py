from Bank.bank import Bank
from src.save import *
from Branch.branch import Branch

class Admin():
    def __init__(self, name, family, national_code, password):
        self.name = name
        self.family = family
        self.national_code = national_code
        self.password = password
        save_password(password)


    def show_data(self, bank: Bank, branch: Branch):
        bank.show_details()
        branch.show_details()


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


    def determine_budget(self, branch: Branch):
        budget = int(input("Enter the budget of this branch: "))
        branch.budget = budget
        save_branch(branch.name, branch.bank_id, branch.number_of_customers, budget, branch.city_name)
        


    def change_password(self):
        current_password = input("Enter your current password")
        if current_password == self.password:
            new_password = input("Enter your new password: ")
            self.password = new_password
        else:
            print("This is not your current password!")