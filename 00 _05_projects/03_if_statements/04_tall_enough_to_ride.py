"""
This program asks the user for their height and checks if they are tall enough 
to ride based on the required minimum height. If the user's height is equal to 
or greater than the required height, they can ride; otherwise, they cannot.
"""

max_height = 50
user_height = float(input("How tall are you?: "))
if user_height >= max_height:
    print("You're tall enough to ride!")
else:
    print("You're not tall enough to ride, but maybe next year!")    