import random

def choose_word():
    words = ["python", "hangman", "developer", "programming", "algorithm", "data"]
    return random.choice(words)

def display(hidden_word, wrong_guesses, lives):
    print(f"Word: {' '.join(hidden_word)}")
    print(f"Wrong guesses: {', '.join(wrong_guesses)}")
    print(f"Lives left: {lives}")

def play_hangman():
    word = choose_word()
    hidden_word = ['_'] * len(word)
    wrong_guesses = []
    lives = 6

    print("Welcome to Hangman!")

    while lives > 0 and "_" in hidden_word:
        display(hidden_word, wrong_guesses, lives)
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a valid single letter.")
            continue

        if guess in wrong_guesses or guess in hidden_word:
            print(f"You already guessed '{guess}'. Try a different letter.")
            continue

        if guess in word:
            for i in range(len(word)):
                if word[i] == guess:
                    hidden_word[i] = guess
            print(f"Good guess! '{guess}' is in the word.")
        else:
            wrong_guesses.append(guess)
            lives -= 1
            print(f"Wrong guess! '{guess}' is not in the word.")

    if "_" not in hidden_word:
        print(f"Congratulations! You've guessed the word: {''.join(hidden_word)}")
    else:
        print(f"Game over! The word was '{word}'.")

if __name__ == "__main__":
    play_hangman()