import random

# game choices :

choices = ["rock" , "paper", "scissors"]

# palyer choice :
player_choice = input("Enter rock , paper, or scissors: ").lower()

# computer choice :
computer_choice = random.choice(choices)

# winner desision :
if player_choice == computer_choice:
  print(f"dono ki choice {player_choice} tha . Its a tie!")

elif player_choice == "rock" and computer_choice == "scissors":
  print(f"Palyer wins! {player_choice} beats {computer_choice}.")

elif player_choice =="paper" and computer_choice == "rock":
  print(f"Palyer wins! {player_choice} beats {computer_choice}.")

elif player_choice =="scissor" and computer_choice == "paper":
  print(f"Palyers win! {player_choice} beats {computer_choice}.")

else:
  print(f"Computers wins! {computer_choice} beats {player_choice}.")