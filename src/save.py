def save_bank(bank_name, bank_id):
    with open("Bank.txt", "w") as file:
        file.write(f"Bank: {bank_name} {bank_id}\n")


def save_branch(name, bank_id, number_of_customers, budget, city_name):
    with open("Branch.txt", "w") as file:
        file.write(f"Branch: {name} {bank_id}, {number_of_customers}, {budget}, {city_name}\n")


def save_password(password):
    with open("Password.txt", "w") as file:
        file.write(f"Password: {password}\n")