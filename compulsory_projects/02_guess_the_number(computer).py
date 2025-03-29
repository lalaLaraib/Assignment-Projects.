# 1 to 50 numbers:



import random
def guess_the_number():
  """Guess The Number Game By Computer"""
  number = random.randint(1,50)
  guesses_left = 7

  # Welcome message:
  print("Welcome to the guess the number game")
  print("I am thinking a number between 1 to 50.")

  # Loop genrated:
  while guesses_left > 0:
    print(f"\nYou have {guesses_left} guesses left.")
    try:
     guess = int(input("Take a guess of another number: "))
    except ValueError:
        print("Invalid input: Please enter a number.")
        continue

    # Guess the secret number:
    if guess < number:
        print("Too low number . Tell me another number!")
    elif guess > number:
        print("Too high number . Tell me another number!")
    else:
        print(f"Congratulations! You got the correct number in {7 - guesses_left + 1} tries.")
        return # Exit the game

    guesses_left -= 1
  print(f"\nYou ran out of guesses. The number was {number}.")


guess_the_number()