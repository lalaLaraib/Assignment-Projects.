"""
This program is calculating to total triangle 
parameter based on user input.
"""
def calculate__triangle_perimeter():
    user_input1 = float((input("What is the Length of side 1?: ")))
    user_input2 = float((input("What is the Length of side 2?: ")))
    user_input3 = float((input("What is the Length of side 3?: ")))
    total_sum = user_input1 + user_input2 + user_input3
    print(f"The perimeter of the triangle is {total_sum:.2f}")
calculate__triangle_perimeter()