from src.check_password_for_admin import check_password_for_admin
from Customer.customer import Customer
from Admin.admin import Admin
from src.get_customer_details import get_customer_details

def menu():
    role = input("\n\nWelcome to the BANK\n\nIf you are a user please enter number 1 and if you are admin enter 2 to enter: ")

    if role == "1":
        user = int(input("If you have an account enter 1 and if you are new please enter 2: "))
        if user == 1:
            national_code = int(input("Please enter your National code to enter: "))
            customer = get_customer_details(national_code)
            print(f"Hi {customer.name}\n\n")
            print("Enter the number of your request\n")
            request_code = int(input("1.Request loan\n2.Deposit\n3.Withdraw"))

            if request_code == 1:
                customer.loan_request(customer[2], customer[3], customer[4])
            elif request_code == 2:
                deposit_amount = int(input("Please enter the amount of money you want to deposit: "))
                customer.deposit(deposit_amount, customer[2], customer[3])
            elif request_code == 3:
                withdraw_amount = int(input("Please enter the amount of money you want to withdraw: "))
                customer.withdraw(withdraw_amount, customer[2], customer[3])
            else:
                print("Exception!!!")
        else:
            print("WELCOME\n")
            customer_name = input("Please enter your name: ")
            customer_family = input("Please enter your family name: ")
            customer_natinal_code = int(input("Please enter your national code: "))
            customer_home_town = input("Please enter your home town: ")
            customer = Customer(customer_name, customer_family, customer_natinal_code, customer_home_town)
            print("First you have to apen an account\n")

            with open("Branch.txt", "r") as file:
                text = file.readlines()
                text = ''.join(text)
                print(text)

            customer_branch = input("Please enter the name of branch you want to have your account in it: ")
            customer.open_acccount(customer_branch)
            print("Your account just create\n")
            print("Enter the number of your request\n")
            request_code = int(input("1.Request loan\n2.Deposit\n3.Withdraw"))

            if request_code == 1:
                customer.loan_request(customer.account_number, customer.account_amount, customer.customer_branch)
            elif request_code == 2:
                deposit_amount = int(input("Please enter the amount of money you want to deposit: "))
                customer.deposit(deposit_amount, customer.account_number, customer.account_amount)
            elif request_code == 3:
                withdraw_amount = int(input("Please enter the amount of money you want to withdraw: "))
                customer.withdraw(withdraw_amount, customer.account_number, customer.account_amount)
            else:
                print("Exception!!!")
    else:
        password = input("Enter the password: \n\n")
        result = check_password_for_admin(password)

        if result == "Succeed\nHi Alireza.P":
            admin = Admin("Alireza", "Pakravan", 2283063991, "Alireza1234509876")
            print("Enter the number of your request\n")
            request_code = int(input("1.Create bank\n2.Create branch\n3.Determine budget\n4.Change password\n"))

            if request_code == 1:
                admin.create_bank()
            elif request_code == 2:
                admin.create_branch()
            elif request_code == 3:
                admin.determine_budget()
            elif request_code == 4:
                admin.change_password()
            else:
                print("Exception!!!")
