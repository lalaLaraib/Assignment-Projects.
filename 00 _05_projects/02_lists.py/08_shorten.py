"""
This program collects user input to create a list and ensures its length does not exceed 3.  
The `shorten` function removes extra elements from the end if the list is longer than 3 items.  
"""

def shorten(lst):
    max_length = 3
    if len(lst) > max_length:
        while len(lst) > max_length:
            trim_list = lst.pop()
            print("Removed:", trim_list)
    else:
        print("No elements removed.")
    print("Final List:",lst)    
    return lst

def get_list():
    my_list = []
    count = 1
    user_input = input(f"Enter a value {count} (or press Enter to stop): ")
    while user_input != "":
        my_list.append(user_input)
        count += 1
        user_input = input(f"Enter a value {count} (or press Enter to stop): ")
        
    return my_list
user_list = get_list()
shorten(user_list)    
    