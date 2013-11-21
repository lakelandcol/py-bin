class Test:
  def __init__(self):      #self = object name
	self.x = 4
	self.y = 5
  def set_value(self, arg):      #arg = what the function expects for input; self is put in automatically
	self.x = arg
	self.z = 1
	print arg
  def print_value(self, arg):
	print self.x
	self.a = 2
	self.b = 3

testObject = Test()   #object name = class name #parenthesis means you call the function or class; necessary for object assignment
testObject.print_value(0)
testObject.set_value(20)
testObject.print_value()
print testObject.x, testObject.z, testObject.a, testObject.b