#!/bin/bash

# Written By Collin Lakeland

# Completed on September 15th, 2013

# Searches current directory for a given file

echo "What is the filename?"     #Should replace this with getopts
echo
read filename
if [ ! $filename  ]

#Used ! argument for the Bash builtin "test" (see man page for builtins, under "test" section) 

then    
    echo "Give me a filename!"
    exit
    
else
    find $filename > /dev/null
    if [ $? = 0 ] 
    
    then
		echo "The file '$filename' exists and here is what it looks like:"
		echo
		sleep 3s  
		echo
		more $filename
	else
		echo
		echo 'The given file does not exist in the present working directory.'    
    
	fi
fi
