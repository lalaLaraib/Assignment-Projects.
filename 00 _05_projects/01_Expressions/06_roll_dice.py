"""
This program, Simulate rolling two dice, and prints results of each roll as well as the total.

"""

import random

rolling_num = 6
def dice_roll():
    dice1 = random.randint(1, rolling_num)
    dice2 = random.randint(1, rolling_num)
    total = dice1 + dice2    
    print(f"Dice have {rolling_num} each sides.")
    print(f"first die: {dice1}")
    print(f"second die: {dice2}")
    print(f"Total sum of two dice is {total}")
dice_roll()   
