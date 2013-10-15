# Written By Collin Lakeland

# Program to solve a quadratic in standard form

from __future__ import division 
import math

try:

    a, b, c= input("Please enter the coefficents: ")

except TypeError:
    
    pass

try:

    x = (-b + math.sqrt((b**2)-4*a*c))/(2*a)          #First root

    x2 = (-b - math.sqrt((b**2)-4*a*c))/(2*a)         #Second Root

except NameError:
    
    b= 0                  #Fix NameError in line 28, says x isnt defined when run with just "a" as coefficent
    
    c= 0

if x == x2 and (-b + math.sqrt((b**2)-4*a*c))%(2*a) == 0:   
    
    print "Your solution is: x =", int(x)
    
elif (-b + math.sqrt((b**2)-4*a*c))%(2*a) == 0 and (-b - math.sqrt((b**2)-4*a*c))%(2*a) == 0:    
    
    print "Your solutions are: x =", int(x), "and x =", int(x2)

elif (-b + math.sqrt((b**2)-4*a*c))%(2*a) == 0:
    
    print "Your solution is: x =", int(x) 
                                                            #Allow imaginary solutions   
elif (-b - math.sqrt((b**2)-4*a*c))%(2*a) == 0:
    
    print "Your solution is: x =", int(x2)
    
elif x == x2:
    print "Your solution is: x = ", x
    
else:
    print "Your solutions are: x =", x, "and x =", x2
    
print a,b,c