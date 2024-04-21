def save_bank(bank_name, bank_id):
    with open("Bank.txt", "w") as file:
        file.write(f"Bank: {bank_name} {bank_id}\n")


def save_branch(name, bank_id, number_of_customers, budget, city_name):
    with open("Branch.txt", "a") as file:
        file.write(f"Branch: {name} {bank_id}, {number_of_customers}, {budget}, {city_name}\n")


def save_password(password):
    with open("Password.txt", "w") as file:
        file.write(f"Password: {password}\n")


def save_account(full_name, national_code, account_number, account_amount, branch_name):
    with open("Account.txt", "a") as file:
        file.write(f"Account: {full_name} with national code of {national_code} and account number of {account_number} has {account_amount} in their account in {branch_name} branch\n")