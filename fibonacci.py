#!/usr/bin/env python3

# Fibonacci Sequence Exercise
# TODO: (Read detailed instructions in the Readme file)
# Prompt the user for the number of terms.
# Validate that the input is a positive integer.
# Use a for loop to print the Fibonacci sequence up to that many terms.

#i rewrote from lab 3 using a function instead

def fibonacci(term):
    sequence =[]
    n1=0
    n2= 1
    if term==1:
        sequence.append(n1)
    else:
        sequence = [n1, n2]
        for _ in range(2, term):
            nth = n1 + n2
            sequence.append(nth)
            n1, n2 = n2, nth
    return sequence
    
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

def prints(sequence):
    print("the fibonacci sequence is:")
    print(sequence)

terms = get_input()
fib_sequence = generate_fibonacci(terms)
print_sequence(fib_sequence)
