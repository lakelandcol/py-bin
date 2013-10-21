# Written By Collin Lakeland

# Program to solve a quadratic in standard form

from __future__ import division      #division module makes it so the division operator doesn't round the quotient
import cmath                               
                                     #cmath module allows for complex solutions

print "Your equation must be in standard form"

print

print "Note that j = i = (-1)^1/2"

print

try:

    a, b, c= input("Please enter the coefficents with the format a,b,c: ")

except TypeError:
    
    pass

try:

    x = (-b + cmath.sqrt((b**2)-4*a*c))/(2*a)          #First root

    x2 = (-b - cmath.sqrt((b**2)-4*a*c))/(2*a)         #Second Root

except NameError:
    
    b= 0                  
    
    c= 0
    
    x = (-b + cmath.sqrt((b**2)-4*a*c))/(2*a)  #Says "a" is not defined here, fix so only "a" can be used for input
    
    x2 = (-b - cmath.sqrt((b**2)-4*a*c))/(2*a)

if x == x2 and (-b + cmath.sqrt((b**2)-4*a*c))%(2*a) == 0:    
    
    print "Your solution is: x =", int(x)                           #Double, integer root
    
elif (-b + cmath.sqrt((b**2)-4*a*c))%(2*a) == 0 and (-b - cmath.sqrt((b**2)-4*a*c))%(2*a) == 0: 
 
    print "Your solutions are: x =", int(x), "and x =", int(x2)       #Distinct integer roots 

elif (-b + cmath.sqrt((b**2)-4*a*c))%(2*a) == 0:
    
    print "Your solution is: x =", int(x)
            
elif (-b - cmath.sqrt((b**2)-4*a*c))%(2*a) == 0:      #lines 49-55, one root is an integer, the second root is not
    
    print "Your solution is: x =", int(x2)
    
elif x == x2:
    print "Your solution is: x = ", x                    #Double, non-integer root
    
else:
    print "Your solutions are: x =", x, "and x =", x2    #Distinct, non-integer roots