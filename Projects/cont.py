

class Account:

    def __init__(self, balance=0):
        self.balance = balance

    def __str__(self):
        return f'Account balance: {self.balance}'

    def balance(self):
        return self.balance

    def deposit(self, suma):
        self.balance += suma
        return 'Deposit accepted'

    def withdraw(self, suma):
        if suma < self.balance:
            self.balance -= suma
            return 'Withdrow accepted'
        else:
            return 'Funds Unavailable!'
