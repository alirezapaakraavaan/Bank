class Bank():
    def __init__(self, name, bank_id):
        self.name = name
        self.bank_id = bank_id


    def show_details(self):
        with open("Bank.txt", "r") as file:
            text = file.readlines()
            text = ''.join(text)
            print(text)