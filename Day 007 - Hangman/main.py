from words import word_list
from art import stages, logo
import random

# -------------------------------------------------
print(logo)
print("Welcome to Hangman!\n")

while True:
    # === NEW GAME SETUP ===
    word_to_guess = random.choice(word_list).lower()
    word_length = len(word_to_guess)
    display = ["_"] * word_length
    guessed_letters = []
    lives = 6

    print("Good luck!\n")

    # === MAIN GAME LOOP ===
    while "_" in display and lives > 0:
        print(stages[lives])
        print("Word: " + " ".join(display))
        print(f"Lives left: {lives}")
        if guessed_letters:
            print(f"Guessed letters: {', '.join(sorted(guessed_letters))}\n")
        else:
            print()

        # Get player guess
        guess = input("Guess a letter: ").strip().lower()

        # Input validation
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter (a-z).")
            continue
        if guess in guessed_letters:
            print("You already guessed that letter!")
            continue

        guessed_letters.append(guess)

        # Check if the guess is in the word
        if guess in word_to_guess:
            for i in range(word_length):
                if word_to_guess[i] == guess:
                    display[i] = guess
            print(f"Correct! '{guess}' is in the word.\n")
        else:
            lives -= 1
            print(f"Sorry, '{guess}' is not in the word.")
            print(f"Lives left: {lives}\n")

    # === GAME OVER ===
    print(stages[lives])

    if lives == 0:
        print(f"You lost! The word was: {word_to_guess.upper()}")
    else:
        print(" ".join(display))
        print(f"Congratulations! You guessed '{word_to_guess.upper()}' correctly!")

    # === PLAY AGAIN? ===
    while True:
        again = input("\nDo you want to play again? (y/n): ").strip().lower()
        if again in ["y", "n"]:
            break
        print("Please answer 'y' or 'n'.")
    
    if again != "y":
        print("\nThanks for playing! Goodbye!")
        break

    print("\n" + "="*50 + "\n")