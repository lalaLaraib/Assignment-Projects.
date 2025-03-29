"""
This program takes multiple numbers as input from the user and stores them in a list.  
It then counts how many times each number appears and displays the results.
"""

def count_nums():
    lst = []
    user_input = input("Enter a number (or press Enter to stop): ")
    while user_input != "":
        try:
            lst.append(int(user_input))
        except ValueError:
             print("Invalid input. Please enter a valid number.")
        user_input = input("Enter a number (or press Enter to stop): ")
    return lst    

def count_occurances(count_num):
    count_dict = {}
    for num in count_num:
        count_dict[num] = count_dict.get(num, 0) + 1
    for num, count in count_dict.items():
        print(f"{num} appears {count} times.")
    return count_dict
    

numbers = count_nums()
count_occurances(numbers)