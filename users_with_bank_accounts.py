class BankAccount:
    def __init__(self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self,amount):
        self.balance -= amount
        return self
    
    def display_account_info(self):
        print(f'Interest Rate: {self.int_rate}, Balance:${self.balance}')
        return self

    def yield_interest(self):
        self.balance *= self.int_rate
        return self

class User:
    def __init__(self, name, email_address, int_rate, balance):
        self.name = name
        self.email_address = email_address
        self.account = BankAccount
    
    def make_deposit(self,amount):
        self.account.deposit(self, amount)

    def make_withdrawal(self,amount):
        self.account.withdraw -= amount
    
    def display_user_balance(self):
        print(f'User: {self.name}, Balance:${self.account.balance}')

    def transfer_money(self, other_user, amount):
        self.make_withdrawal(amount)
        other_user.make_deposit(amount)