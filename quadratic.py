# Written By Collin Lakeland

# Program to solve a quadratic in standard form

from __future__ import division      #division module makes it so the division operator doesn't round the quotient
import cmath                         #cmath module allows for complex solutions
import sys, getopt

#class here

class Quadratic():
  
  def __init__(self, argv):
	self.args = argv                            #This is where user input occurs
	print args
	a = None
	b = None
	c = None
	x = (-b + cmath.sqrt((b**2)-4*a*c))/(2*a)          #First root

	x2 = (-b - cmath.sqrt((b**2)-4*a*c))/(2*a)         #Second Root

  def length(self):
	if len(self.args) > 3:
	  print "Error: Your equation must be in standard form."
	elif len(self.args) == 3:
	  a = self.args[0]
	  b = self.args[1]
	  c = self.args[2]
	elif len(self.args) == 1:
	  a = self.args[0]
	  b = 0
	  c = 0


  def testing(x, x2):
	if x == x2 and x.imag == 0:
	  print "Your solution is: x=", x.real                    #Double, real root

	elif x.imag == 0 and x2.imag == 0:                        #Distinct real roots
	  print "Your solutions are: x=", x.real, "and x=", x2.real
  
	elif x == x2:
	  print "Your solution is: x = ", x                       #Double, complex root
    
	else:
	  print "Your solutions are: x =", x, "and x =", x2       #Distinct, complex root

solverObject = Quadratic(sys.argv[1:])

solverObject.testing(x, x2)

print "Your equation must be in standard form"

print

print "Note that j = i = (-1)^1/2"

print

#WARNING *PSUEDOCODE*
"""
inputList = they entered stuff here
a = None
b = None
c = None
 
if len(inputList) > 3:
        error and ask them to try again
else
        if len(inputList) == 1:
                a = inputList[0]
                b = 0
                c = 0
        elif len(inputList) == 2:
                a = inputList[0]
                b = inputList[1]
                c = 0
        else
                a = inputList[0]
                b = inputList[1]
                c = inputList[2]
"""
#End of pseudocode


#WARNING *Unused code*

#x = cmath.sqrt(a)              #Funny lines
  
#testing(x, x2)
  
#else:
	#testing(x, x2)
"""

  if x == x2 and x.imag == 0:
	print "Your solution is: x=", x.real             #Double, real root

  elif x.imag == 0 and x2.imag == 0:                      #Distinct real roots
	print "Your solutions are: x=", x.real, "and x=", x2.real
  
  elif x == x2:
	print "Your solution is: x = ", x   #Double, complex root
    
  else:
	print "Your solutions are: x =", x, "and x =", x2    #Distinct, complex root
"""


          #Fix so that input of the form a,0,0 gives correct solution, says solution is 0 now

          #Fix so input 0,0,0 doesn't error




#if __name__ == "__main__":
   #main(sys.argv[1:])

#Says b isn't defined