# Written By Collin Lakeland

# Program to solve a quadratic in standard form

from __future__ import division      #division module makes it so the division operator doesn't round the quotient
import cmath                         #cmath module allows for complex solutions
import sys

class Quadratic():
  
	def __init__(self, argv):
		self.a = int()
		self.b = int()
		self.c = int()
		
		#user input
		self.coeffs = sys.argv
		print len(self.coeffs)
	#Try block allows input of the form: 0, b ,c, which gives a ZeroDivisionError	
	try:	
	
		def more_than_three_coefficients(self):
			if len(self.coeffs) > 4:
				print "Usage: You must give three coefficents, even if those coefficients are zero, your equation must be of degree 2 or lower, and in standard form."
				sys.exit(0)
		def less_than_three_coefficient(self):
			if self.coeffs < 4:
				print "Usage: You must give three coefficients, even if those coefficents are zero"
				sys.exit(0)
		def three_coefficients(self):
			if len(self.coeffs) == 4:
				self.a = int(self.coeffs[1])
				self.b = int(self.coeffs[2])
				self.c = int(self.coeffs[3])
				
				#These assignments make creating the roots easier.
				a = self.a
				b = self.b
				c = self.c
				print a, b, c
							
				#Root creation
				self.x = (-1*b + cmath.sqrt((b**2)-4*a*c))/(2*a)        #First root
			
				self.x2 = (-1*b - cmath.sqrt((b**2)-4*a*c))/(2*a)       #Second Root
	
	except ZeroDivisionError:
		self.x = 0
		self.x2 = 0			
		print a, b, c
		
	#Tests to see what type of solutions there are.
	def testing(self, x, x2):
		if x == x2 and x.imag == 0:
			print "Your solution is: x =", x.real                    #Double, real root

		elif x.imag == 0 and x2.imag == 0:                        #Distinct real roots
			print "Your solutions are: x =", x.real, "and x =", x2.real
  
		elif x == x2:
			print "Your solution is: x = ", x                       #Double, complex root
    
		else:
			print "Your solutions are: x =", x, "and x =", x2       #Distinct, complex root

solverObject = Quadratic(sys.argv[1:])
solverObject.three_coefficients()       #Must I call every method within the class? What happens when they put in 1 or 2 coefficients?
solverObject.testing(solverObject.x, solverObject.x2)

print "Your equation must be in standard form"

print

print "Note that j = i = (-1)^1/2"

print

#sys.argv[2:]
