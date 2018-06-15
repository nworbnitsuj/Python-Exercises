

class BankAccount():
    def __init__(self):
        self.balance = 0
        self.interest = 0.02

    def deposit(self, amount):
        if(amount < 0):
            print('False')
        else:
            self.balance += amount

    def withdraw(self, amount):
        if(amount < 0):
            print('False')
        self.balance -= amount

    def accumulate_interest(self):
        self.balance = ((self.balance * self.interest) + self.balance)
