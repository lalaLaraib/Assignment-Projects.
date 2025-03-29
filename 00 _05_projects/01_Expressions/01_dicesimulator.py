"""
This program simulates rolling two dice multiple times 
and prints the total sum of both dice for each roll.

"""

import random

num_rolls = 3

def roll_dice():
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    total = dice1 + dice2    
    print(f"Total sum of two dice is {total}")
for i in range(num_rolls):      
 roll_dice()
    