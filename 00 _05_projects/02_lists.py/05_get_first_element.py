"""
This program takes user input to create a list and prints its first element.  
The `get_list` function collects inputs, and `get_first_element` prints the first item.  

"""
def get_first_element(first_element):
    print("First Element:", first_element[0])

def get_list():
    lst = []
    user_input= input("Please enter an element of the list or press enter to stop. ")
    while user_input != "":
        lst.append(user_input)
        user_input = input("Please enter an element of the list or press enter to stop. ")
    print(lst)
    return lst    
    
my_list = get_list()    
get_first_element(my_list)