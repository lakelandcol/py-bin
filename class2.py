class MyClass:
  
  def __init__(self):
    self.i = "foo"

  def printOut(self):
    print self.i

obj = MyClass()

print obj.i
obj.printOut()
