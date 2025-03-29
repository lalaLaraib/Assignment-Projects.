"""
This function prints all even numbers from 0 to 39.  
It checks if a number is divisible by 2 and prints it.
"""

def print_evens():
    for i in range(0, 40):
        if i % 2 == 0:
            print(i, end=" ")
print_evens()