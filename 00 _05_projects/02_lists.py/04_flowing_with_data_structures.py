"""
This program shows how lists (mutable data types) can be modified inside a function.
The `three_copies` function adds three copies of the given data to the list.  
Since lists are mutable, the changes remain even outside the function.  
"""

def three_copies(List, data):
    for i in range(3):
        List.append(data)

user_input = input("Enter a message to copy: ")
my_list = []
print("List Before", my_list)

three_copies(my_list, user_input)
print("List After", my_list)