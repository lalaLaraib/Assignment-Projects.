"""
This program calculates the hypotenuse of a right-angled triangle using 
the Pythagorean Theorem:
c² = a² + b²
c = sqrt(a² + b²)

"""

import math

def pythagoras_theorem():
    side_ab = float(input("Enter the length of side AB: "))
    side_bc = float(input("Enter the length of side BC: "))
    pythagoras = math.sqrt(side_ab ** 2 + side_bc ** 2)
    print(f"The length of side AC is: {pythagoras}")
pythagoras_theorem()    