#Written By Collin Lakeland

#Program to solve any equation using Newton's Method

from __future__ import division 		#division module makes it so the division operator doesn't round the quotient
import cmath                    		#cmath module allows for complex solutions

class Solver:

	def __init__(self):
		print "Your equation must be set equal to zero"
		#user input
		equation = raw_input("Input your equation: ")
		print equation     #Debugging purposes
		guess = raw_input("Guess the solution:\n")
		print guess
	#def derivative(self, equation):


	#def Newtons_method(self, equation, guess):

solverObject = Solver()
"""
print "Input your equation"

**They input it, exactly as is**

store eqation

Define the derivative of the equation

print "Now take a guess, your guess must be close to what the solution actually is"

**They guess**

Process ( guess - (equation)/(derivative) ) in a loop a high number of times, for a high degree of accuracy    **Newton's Method**

Store solution

print "Your solution is", solution

Repeat this process until all solutions are found    If the highest degree is an integer, then the number of solutions will equal this integer (when double roots are included)

print "Your solutions are:", solution1, solution2, solution3....solution-N  **Possibly in a column**

"""

