class Test:
  def set_value(self):
	self.x = 4
	self.y = 3
  def print_value(self):
	#self.m = 9
	print self.x

testObject = Test()
testObject.set_value()
testObject.print_value()