def get_customer_details(national_code):
    with open("Account.txt", "r") as file:
        text = file.readlines()
        text = ''.join(text)

        if national_code in text:
            details = text.strip()
            return details
        else:
            return "Not found!"