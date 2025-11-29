import random
from art import choices

print("Welcome to the Rock Paper Scissors Game!")

# Getting user choice
user_choice = int(input("Enter your choice:\n" \
                        "0 - Rock\n" \
                        "1 - Paper\n" \
                        "2 - Scissors\n"))

print(f"\nUser choice:\n{choices[user_choice]}")

# Setting computer choice
computer_choice = random.randint(0, 2)
print(f"Computer choice:\n{choices[computer_choice]}")

# Game logic
if user_choice == computer_choice:
    print("It's a tie.")
elif (user_choice == 0 and computer_choice == 2) or \
     (user_choice == 1 and computer_choice == 0) or \
     (user_choice == 2 and computer_choice == 1):
    print("Congrats. You Win!")
else:
    print("You Lose. Game Over")
