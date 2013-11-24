class BankAccount():              #Does an argument here get assigned to initial balance?
	def __init__(self, initial_balance=0):
		self.balance = initial_balance
		print initial_balance                                #Important line
	def deposit(self, amount):
		self.balance += amount
	def withdraw(self, amount):
		self.balance -= amount
	def overdrawn(self):          #What does this method do?
		return self.balance < 0
my_account = BankAccount(20)   #This is where an object is created

my_account.__init__(8)
print my_account.balance



#object.variable name (Python puts in self for you)
