import random

def loan_number_generator():
    return random.randrange(10**(8-1), 10**8)