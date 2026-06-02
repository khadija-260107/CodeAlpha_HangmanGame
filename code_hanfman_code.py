# =============================================
# TASK 1: HANGMAN GAME
# CodeAlpha Internship — Python Programming
# =============================================

import random

# A more realistic word list with categories
words = [
    "programming", "algorithm", "database", "internet", "keyboard",
    "software", "hardware", "network", "variable", "function"
]

# Visual hangman stages — shows the hangman being drawn step by step
hangman_stages = [
    """
       -----
       |   |
           |
           |
           |
           |
    =========""",
    """
       -----
       |   |
       O   |
           |
           |
           |
    =========""",
    """
       -----
       |   |
       O   |
       |   |
           |
           |
    =========""",
    """
       -----
       |   |
       O   |
      /|   |
           |
           |
    =========""",
    """
       -----
       |   |
       O   |
      /|\\  |
           |
           |
    =========""",
    """
       -----
       |   |
       O   |
      /|\\  |
      /    |
           |
    =========""",
    """
       -----
       |   |
       O   |
      /|\\  |
      / \\  |
           |
    ========="""
]

def play_hangman():
    secret_word = random.choice(words)
    display = ["_"] * len(secret_word)
    guessed_letters = []
    wrong_guesses = 0
    max_wrong = 6

    print("\n" + "=" * 45)
    print("          HANGMAN GAME")
    print("=" * 45)
    print(f"The word has {len(secret_word)} letters.")

    while wrong_guesses < max_wrong and "_" in display:

        # Show hangman drawing
        print(hangman_stages[wrong_guesses])

        # Show current word progress
        print("\nWord: " + " ".join(display))
        print(f"Wrong guesses: {wrong_guesses}/{max_wrong}")
        print(f"Letters used:  {', '.join(sorted(guessed_letters))}")

        # Get valid single letter input
        while True:
            guess = input("\nEnter a letter: ").lower().strip()
            if len(guess) != 1:
                print("Please enter a single letter only.")
            elif not guess.isalpha():
                print("Please enter a letter, not a number or symbol.")
            elif guess in guessed_letters:
                print(f"You already guessed '{guess}'. Try a different one.")
            else:
                break

        guessed_letters.append(guess)

        if guess in secret_word:
            print(f"Correct! '{guess}' is in the word.")
            for i in range(len(secret_word)):
                if secret_word[i] == guess:
                    display[i] = guess
        else:
            wrong_guesses += 1
            print(f"Wrong! '{guess}' is not in the word.")

    # Final result
    print(hangman_stages[wrong_guesses])

    if "_" not in display:
        print("\nRESULT: You won!")
        print(f"The word was: {secret_word}")
    else:
        print("\nRESULT: You lost.")
        print(f"The word was: {secret_word}")

    print("=" * 45)

    # Ask to play again
    again = input("\nPlay again? (yes / no): ").lower()
    if again == "yes":
        play_hangman()
    else:
        print("Thanks for playing. Goodbye.")

# Run the game
play_hangman()
