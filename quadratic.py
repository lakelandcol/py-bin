# Written By Collin Lakeland

# Program to solve a quadratic in standard form

from __future__ import division      #division module makes it so the division operator doesn't round the quotient
import cmath                               
                                     #cmath module allows for complex solutions
                                     
def testing(x, x2):
  
  if x == x2 and x.imag == 0:
	print "Your solution is: x=", x.real             #Double, real root

  elif x.imag == 0 and x2.imag == 0:                      #Distinct real roots
	print "Your solutions are: x=", x.real, "and x=", x2.real
  
  elif x == x2:
	print "Your solution is: x = ", x   #Double, complex root
    
  else:
	print "Your solutions are: x =", x, "and x =", x2 


print "Your equation must be in standard form"

print

print "Note that j = i = (-1)^1/2"

print

try:

  a, b, c= input("Please enter the coefficents with the format a,b,c: ")

except TypeError:
  
  b= 0
  
  c= 0
  
  x = cmath.sqrt(a)
  
  testing(x, x2)
  
else:

  x = (-b + cmath.sqrt((b**2)-4*a*c))/(2*a)          #First root

  x2 = (-b - cmath.sqrt((b**2)-4*a*c))/(2*a)         #Second Root

  if x == x2 and x.imag == 0:
	print "Your solution is: x=", x.real             #Double, real root

  elif x.imag == 0 and x2.imag == 0:                      #Distinct real roots
	print "Your solutions are: x=", x.real, "and x=", x2.real
  
  elif x == x2:
	print "Your solution is: x = ", x   #Double, complex root
    
  else:
	print "Your solutions are: x =", x, "and x =", x2    #Distinct, complex root

#Fix so that input of the form a,0,0 gives correct solution, says solution is 0 now

#Fix so input 0,0,0 doesn't error