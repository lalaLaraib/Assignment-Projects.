"""
This program manages a list of fruits. It first prints the length of the initial list, 
then adds 'mango' to the list and displays the updated list.
"""

def fruits():
    fruit_list = [ 'apple', 'banana', 'orange', 'grape', 'pineapple']
    print("The length of the list is", len(fruit_list))
    fruit_list.append("mango")
    print("After adding a fruit, the list is", fruit_list)
fruits()    