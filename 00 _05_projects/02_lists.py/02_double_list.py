"""
    This function takes a list of integers and returns a new list with each
    element doubled.
    """

def double_list(numbers:list[int]):
    doubled_list = []
    for double in numbers:
        doubled_list.append(double*2)
    return doubled_list
    
numbers = [2, 4, 6, 8, 10] 
result = double_list(numbers)
print(f"The doubled list is {result}")

  