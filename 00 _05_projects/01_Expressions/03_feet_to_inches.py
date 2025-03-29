"""
This program converts feet to inches using a simple conversion formula:
inches = feet * 12 where 1 foot = 12 inches (constant value)

"""

one_foot = 12

def feet_to_inches():
    user_input = float(input("Enter the number to convert in inches: "))
    conversion = user_input * one_foot
    print(f"{user_input} feet is equal to {conversion} inches.")

feet_to_inches()    