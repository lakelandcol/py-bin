class Test:
  def __init__(self):      #self = object name
	self.x = 4
	self.y = 5
  def set_value(self, arg, c):      #arg = an argument = what the function expects for input; self is put in automatically
	self.x = arg
	self.z = 1
	print c
  def print_value(self, arg):
	#print self.x
	self.a = 2
	self.b = 3

testObject = Test()    #SYNTAX:  object name = class name; parenthesis means you call the function or class, this is necessary for object assignment
#testObject.print_value(0)
print testObject.x
testObject.print_value(1)
testObject.set_value(20, 1)
print testObject.x, testObject.z, testObject.a, testObject.b

#ASSIGNMENTS:
#    = *new name* = *old name*
