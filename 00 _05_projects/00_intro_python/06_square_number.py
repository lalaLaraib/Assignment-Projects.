"""
In this program user will enter the number
to see the square of that number.
"""

def square_number():
    user_input = float(input("Enter the number you want to square: "))
    square = user_input ** 2
    print(f"The square of {user_input} is {square}")

square_number()