"""
This program takes user input to create a list. The `get_list` function collects 
values and displays the final list after input stops.  
"""

def get_list():
    my_list = []
    count = 1
    user_input = input(f"Enter a value {count}: ") 
    while user_input != "":
            my_list.append(user_input)
            count += 1  # Increment count for next input prompt
            user_input = input(f"Enter a value {count}: ")
    print(my_list)
    return my_list
get_list()