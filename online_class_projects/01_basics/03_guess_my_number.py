"""
A number guessing game where the user has to guess a randomly generated number.
"""

import random
def guess_number():
    print("I am thinking of a number between 1 and 99:")
    secret_number = random.randint(1, 99)
    
    while True:
        guess = int(input("Guess the number: "))
        if guess_number < 0 or guess_number > 99:
                print("Please enter a number between 1 and 99.")
                continue
        try:    
            if  guess < secret_number:
                print("Your guess is too low")
            elif guess > secret_number:
                print("Your guess is too high")
            else:
                print(f"Congratulations! You guessed the {secret_number} correct number.")
                break    
        except ValueError:
             print("Please Enter a valid input!")    
guess_number()