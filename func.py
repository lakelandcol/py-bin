class Test:
	def __init__(self):      #self = object name
		self.x = 4
		self.y = 5
	def set_value(self, arg, c):      #arg = an argument = what the function expects for input; self is put in automatically
		self.x = arg
		self.z = 1
		print c
	def print_value(self, arg):
		print self.x
		self.a = 2
		self.b = 3
	def variables (self):
		self.g = 9
testObject = Test()    #SYNTAX:  object name = class name; parenthesis means you call the function or class, this is necessary for object assignment
#testObject.print_value(0)
#print testObject.x
testObject.print_value(1)
#testObject.set_value(20, 1)
#testObject.variables()
#print testObject.x, testObject.z, testObject.a, testObject.b, testObject.g

#ASSIGNMENTS:
#    = *new name* = *old name*
