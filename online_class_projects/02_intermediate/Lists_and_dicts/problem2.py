"""
This program allows users to interact with a list by performing three operations:
1. Accessing an element by index.
2. Modifying an element at a specific index.
3. Slicing the list within a given range.
It handles potential index errors gracefully.
"""

lst = ["apple", "orange", "banana", "kiwi", "mango"]

def access_list(lst, index):
    try:
        return lst[index]
    except IndexError:
        return "Index out of range"

def modify_list(lst, index, value):
    try:
        lst[index] = value
        return lst
    except IndexError:
        return "Index out of range"

def slice_list(lst, start, end):
    try:
        return lst[start:end]
    except IndexError:
        return "Invalid indices."    
        
def index_game():
    print("current List:", lst)
    operation_input = input("Enter the operation you want (access, modify, slice): ")
    if operation_input == "access":
        index = int(input("Enter index to access: "))
        print(access_list(lst, index))
    elif operation_input == "modify":
        index = int(input("Enter index to modify: "))
        value = input("Enter value: ")
        print(modify_list(lst, index, value))
    elif operation_input == "slice":
        start = int(input("Enter start index: "))
        end = int(input("Enter end index: "))
        print(slice_list(lst, start, end))
    else:
        print("Invalid operation.")

index_game()            
            