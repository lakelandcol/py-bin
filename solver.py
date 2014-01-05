#Written By Collin Lakeland

#Program to solve any equation using Newton's Method

from __future__ import division 		#division module makes it so the division operator doesn't round the quotient
import cmath                    		#cmath module allows for complex solutions
import sys                      

class Solver():
	
	def __init__(self, argv):
		#user input
		equation = sys.argv[1]
		print equation
		#print len(self.coeffs)   Debugging purposes
"""
print "Input your equation"

**They input it, exactly as is**

store eqation

Define the derivative of the equation

print "Now take a guess, your guess must be close to what the solution actually is"

**They guess**

Process ( guess - (equation)/(derivative) ) recursively a high number of times, for a high degree of accuracy    **Newton's Method**

Store solution

print "Your solution is", solution

Repeat this process until all solutions are found    If the highest degree is an integer, then the number of solutions will equal this integer (when double roots are included)

print "Your solutions are:", solution1, solution2, solution3....solution-N  **Possibly in a column**

"""

