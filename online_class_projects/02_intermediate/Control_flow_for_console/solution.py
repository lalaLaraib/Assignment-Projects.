"""
This is a High-Low game where the player guesses whether their randomly generated number 
is higher or lower than the computer's number. The game consists of 5 rounds, and the 
player earns a point for each correct guess. The final score determines the outcome.
"""

import random

def high_low_game():
   
    print("Welcome to the High-Low Game!")
    print("Lets start the game...")
    print("------------------------------------")
    
    rounds = 5
    score = 0
    for i in range(rounds):
        print(f"Round {i + 1}")
        print("--------------------------")

        computer_num = random.randint(1, 100)
        user_num = random.randint(1, 100)

        print(f"Your Number is {user_num}")
        user_choice = input("Do you think your number is higher or lower than the computer's? (higher/lower): ").strip().lower()

        # check conditions

        high_and_correct = user_choice == "higher" and user_num > computer_num
        low_and_correct = user_choice == "lower" and user_num < computer_num

        if high_and_correct or low_and_correct:
            print(f"You were right! The computer's number was {computer_num}")
            score += 1
            print(f"Your score is {score}")
            print()
        else:
            print(f"Awww, you were wrong! The computer's number was {computer_num}")
            print(f"Your score is {score}")
            print()

    if score == 5:
         print("🎉 You won the game! Excellent performance! 🏆")
         
    else:
        print(f"😢 You lost the game! Your final score is {score}. Try again!")
                            
    
    print(f"Game Over! Your final score is {score}")

high_low_game()    
