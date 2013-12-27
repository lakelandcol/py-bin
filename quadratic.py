#Written By Collin Lakeland

#Program to solve a quadratic in standard form

#Completed on December 20th, 2013

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
		#print len(self.coeffs)     Debugging purposes			
	def more_than_three_coefficients(self):
		if len(self.coeffs) > 4:
			print "Usage: You must give three coefficents, even if those coefficients are zero, your equation must be of degree 2 or lower and in standard form."
			sys.exit()
	def less_than_three_coefficients(self):
		if len(self.coeffs) < 4:
			print "Usage: You must give three coefficients, even if those coefficents are zero, your equation must be of degree 2 or lower and in standard form."
			sys.exit()
	def three_coefficients(self):
		if len(self.coeffs) == 4:
			self.a = int(self.coeffs[1])
			self.b = int(self.coeffs[2])
			self.c = int(self.coeffs[3])
			
	#Tests for specific triplets of coeffcients, which normally give a ZeroDivisonError or some other sort of error.
	def coefficient_type_testing(self):
		if self.a == 0 and self.b != 0:
			#print "condition true"		Debugging purposes
			self.x = -self.c/self.b
			self.x2 = -self.c/self.b		
		
		elif self.a == 0 and self.b == 0 and self.c == 0:
			print self.c,"= 0"
			sys.exit(0)
		elif self.a == 0 and self.b == 0:
			print self.c, "will never equal 0"
			sys.exit(0)
		else:
			#print "condition false"		Debugging purposes    

			#Root creation
			self.x = (-self.b + cmath.sqrt((self.b**2)-4*self.a*self.c))/(2*self.a)		#First root
			
			self.x2 = (-self.b - cmath.sqrt((self.b**2)-4*self.a*self.c))/(2*self.a)	#Second Root
		
	#Tests to see what type of roots there are and prints them accordingly.
	def root_type_testing(self, x, x2):
		if x == x2 and x.imag == 0 and x == -0.0:					#Double, real root
			x = 0.0
			print "Your solution is: x =", x
		
		elif x == x2 and x.imag == 0:
			print "Your solution is: x =", x.real

		elif x.imag == 0 and x2.imag == 0:							#Distinct real roots
			print "Your solutions are: x =", x.real, "and x =", x2.real
		
		elif x == x2:
			print "Your solution is: x = ", x						#Double, complex root
			print "Note that j = i = (-1)^1/2"

		else:
			print "Your solutions are: x =", x, "and x =", x2       #Distinct, complex root
			print "Note that j = i = (-1)^1/2"

solverObject = Quadratic(sys.argv[1:])
solverObject.more_than_three_coefficients()
solverObject.less_than_three_coefficients()
solverObject.three_coefficients()
solverObject.coefficient_type_testing()
solverObject.root_type_testing(solverObject.x, solverObject.x2)
