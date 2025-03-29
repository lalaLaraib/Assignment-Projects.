'''
This program asks the user to enter a number, then keeps doubling it
until the value reaches 100 or more.'
'''

curr_value = float(input("Enter a number: "))
while curr_value < 100:
    curr_value = curr_value* 2
    print(curr_value, end=" ")