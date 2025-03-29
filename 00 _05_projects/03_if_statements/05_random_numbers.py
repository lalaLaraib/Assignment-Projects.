"""
This program generates and prints 10 random numbers in the range of 1 to 100.
Each time the program runs, it produces different random numbers.
"""

import random

for i in range(10):
   print(random.randint(1, 100), end = " ")