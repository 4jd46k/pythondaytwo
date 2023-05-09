class BankAccount:
    def __init__(self, initial_balance=0):
        self.balance = initial_balance
    
    def deposit(self, amount):
        self.balance += amount
    
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Insufficient funds")
    
    def get_balance(self):
        return self.balance

initial_balance = float(input("Enter initial balance: "))
my_account = BankAccount(initial_balance)

deposit_amount = float(input("Enter deposit amount: "))
my_account.deposit(deposit_amount)

withdraw_amount = float(input("Enter withdrawal amount: "))
my_account.withdraw(withdraw_amount)

print("Current balance:", my_account.get_balance())
