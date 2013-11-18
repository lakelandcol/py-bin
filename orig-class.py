class BankAccount(object):
    def __init__(self, initial_balance=0):
        self.balance = initial_balance        #Important line
    def deposit(self, amount):
        self.balance += amount
    def withdraw(self, amount):
        self.balance -= amount
    def overdrawn(self):
        return self.balance < 0
my_account = BankAccount(15)   #This is where an object is created
#my_account.withdraw(5)
print my_account.balance           #object.variable name (Python puts in self for you)
