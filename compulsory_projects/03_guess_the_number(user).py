import random
print("Guess the number between 1 and 100!")
# genrate random number:
number = random.randint(1, 100)

while True:
  guess= int(input("Enter your guess number:"))
  if guess < number:
    print("To Low Number!")
  elif guess > number:
    print("To High Number!")
  else:
    print("Congratulation You Got Right")
    break