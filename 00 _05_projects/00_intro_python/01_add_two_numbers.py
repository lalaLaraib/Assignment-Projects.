"""
This program will take two numbers from user and convert them into integers
and will give the total sum of two numbers.
"""

def sum_of_numbers():
    user_input1 = int((input("Enter the First Number: ")))
    user_input2 = int((input("Enter the Second Number: ")))
    total_sum = user_input1 + user_input2
    print(f"The sum of {user_input1} and {user_input2} is {total_sum}")
sum_of_numbers()