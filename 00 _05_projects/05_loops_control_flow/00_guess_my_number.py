"""
A number guessing game where the user has to guess a randomly generated number.
"""
import random

def guess_my_number():
    secret_number = random.randint(1, 99)
    print("I am thinking of a number between 1 and 99")
    while True:
        try:
            guess_number = int(input("Enter a number you guess: "))
            if guess_number < 0 or guess_number > 99:
                print("Please enter a number between 1 and 99.")
                continue
            if guess_number < secret_number:
                print("Your guess is too low, try another guess.")
            elif guess_number > secret_number:
                print("Your guess is too high, try another guess.")
            else:
                print(f"Congratulations! You guessed the number {secret_number} correctly.")
                break        
        except ValueError:
            print("Invalid input. Please enter a valid number.")
guess_my_number()