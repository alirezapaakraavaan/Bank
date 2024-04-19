class Branch():
    def __init__(self, name=None, bank_id=None, budget=None, city_name=None):
        self.name = name
        self.bank_id = bank_id
        self.number_of_customers = 0
        self.budget = budget
        self.city_name = city_name


    def show_details(self):
        with open("Branch.txt", "r") as file:
            text = file.readlines()
            text = ''.join(text)
            print(text)