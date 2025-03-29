"""
This program defines a function `add_numbers` that takes a list of integers
and returns the sum of all elements in the list.

"""
def add_numbers(numbers:list[int]):
    total = 0
    for num in numbers:
        total += num
    return total

numbers = [1, 2, 3, 4, 5]
result = add_numbers(numbers)
print(f"The sum of all numbers is {result}")
