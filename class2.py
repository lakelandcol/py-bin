class MyClass:
  def __init__(self, x):
	self.i = "You just printed out a variable!"
	#print self.i
	print x, type(x)
	#print "You just defined a variable and printed it out! Good job!"
  #def printOut(self):

obj = MyClass("my variable")
