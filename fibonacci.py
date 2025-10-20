#!/usr/bin/env python3

# Fibonacci Sequence Exercise
# TODO: (Read detailed instructions in the Readme file)
# Prompt the user for the number of terms.
# Validate that the input is a positive integer.
# Use a for loop to print the Fibonacci sequence up to that many terms.

#i rewrote from lab 3 using a function instead

def fibonacci(term):
    n1=0
    n2= 1
    if term==1:
        print("the sequence is:")
        print(n1)
    else:
        print("the sequence is:")
        print(n1)
        print(n2)
        for _ in range(2, term):
            nth = n1 + n2
            print(nth)
            n1, n2 = n2, nth

def getinput():
    while True:
        userinput = input("Type how many terms of the Fibonacci sequence you want here (integers only): ")
        if userinput.isdigit():
            term = int(userinput)
            if term > 0:
                return term
            else:
                print("Please enter a positive number!")
        else:
            print("Invalid input! Please enter an integer.")

terms = getinput()
fibonacci(terms)
