"""
This program calculates the quotient and remainder of a division operation using
user's input.

"""

def remainder_division():

    num1 = float(input("Enter the number to divide by: "))
    num2 = float(input("Enter the number to divide by: "))
    if num2 == 0:
        print("Cannot divide by zero.")
        return
    quotient = num1 // num2
    remainder = num1 % num2
    print(f"{num1} divided by {num2} gives quotient {quotient} and remainder {remainder}.")
remainder_division()    
    