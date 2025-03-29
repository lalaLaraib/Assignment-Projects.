"""
This program takes user input to create a list and prints its last element.  
The `get_list` function collects inputs, and `get_last_element` prints the last item.  
"""

def get_last_element(last_element):
    print("Last Element:", last_element[-1])

def get_list():
    lst = []
    user_input= input("Please enter an element of the list or press enter to stop. ")
    while user_input != "":
        lst.append(user_input)
        user_input = input("Please enter an element of the list or press enter to stop. ")
    print(lst)
    return lst    
    
my_list = get_list()    
get_last_element(my_list)