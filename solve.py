#Written By Collin Lakeland

#Program to solve any equation using Newton's Method

from __future__ import division 		#division module makes it so the division operator doesn't round the quotient
import cmath                           #cmath module allows for complex solutions
import sys

class Solver:

	def __init__(self, argv):
		x = int()
		n = int()   #The power
		print "Your equation must be set equal to zero"
		print "Input the coefficients and the corresponding powers of the terms, even if those coefficients or terms are zero"
		#User input here
		for arg in sys.argv:
			coeffs = sys.argv[1+2*x]  #coefficients are odd arguments
			powers = sys.argv[2+2*x]  #powers are even arguments
		#This is weird
		print coeffs
		print powers
		#print sys.argv[-1]      #HOW DOES THIS WORK
		#print equation     #Debugging purposes
		#guess = raw_input("Guess the solution:\n")
		#print guess
	#def derivative(self, equation):


	#def Newtons_method(self, equation, guess):

solverObject = Solver(sys.argv[1:])

#FIX: HOW TO ALLOW FOR AN INFINITE NUMBER OF COEFFICIENTS AND POWERS, AND ASSIGN THEM UNIQUELY TO A COMMAND ARGUMENT?? MAYBE FOR LOOP??
"""
print "Input coefficients and corresponding powers"


**They input it them, odd command line arguments being coefficients, even command line arguments being powers"   

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

