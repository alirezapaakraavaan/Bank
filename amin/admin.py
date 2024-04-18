class Admin():
    def __init__(self, name, family, national_code, password):
        self.name = name
        self.family = family
        self.national_code = national_code
        self.password = password


    def show_data(self, *args):
        if args == "Bank":
            print("Bank details")
        elif args == "Branch":
            print("Branch details")


    def create_bank(self):
        pass


    def create_branch(self):
        pass


    def determine_budget(self):
        pass


    def change_password(self):
        pass