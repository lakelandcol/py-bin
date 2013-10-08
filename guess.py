#!/usr/bin/python

# Written By Collin Lakeland

# Completed on October 5th, 2013

# This is a simple number guessing game.

import random

guesses_made = 0

name = raw_input("Hello! What is your name?\n")

number = random.randint(1, 20)

print "Well, {0}, I am thinking of a number between 1 and 20.".format(name)

while guesses_made < 6:
    
    try:
    
	x= input("Take a guess: ")
	
	y= type(x)
    
	if y == int:
	    
	    pass
	
	elif y == float:
	    
	    pass
	    
	else:
	    
	    print "Give me a number"
	    
	    break
    
    except (NameError, SyntaxError):
	
	#This "allows" a series of letters not enclosed in quotations to be used without python giving an error, also allows special characters like "^" or "&".
	
	  print "Nice try, give me a number"
	
	  break
    
    guesses_made += 1
    
    if x < number:
        
	print "Duurh, too low, stupid!"
        
    if x > number:
        
	print "Your guess is too high."    
        
    if x == number:
	
	print "You got it! You guessed my number in {1} guesses!".format(name, guesses_made)
	
	break
   
    if guesses_made == 6:
	
	print "You failed. The number I was thinking of was {0}".format(number)
	
	break