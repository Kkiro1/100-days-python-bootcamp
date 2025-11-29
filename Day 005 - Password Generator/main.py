import random
from data import letters, symbols, numbers

print("Welcome th the PyPassword Generator!")

n_letters = int(input("How many letters would you like in your password? "))
n_symbols = int(input("How many symbols would you like in your password? "))
n_numbers = int(input("How many numbers would you like in your password? "))

password_list = []

for _ in range(n_letters):
    password_list.append(random.choice(letters))

for _ in range(n_symbols):
    password_list.append(random.choice(symbols))

for _ in range(n_numbers):
    password_list.append(random.choice(numbers))
    
random.shuffle(password_list)
password = ''.join(password_list)

print(f"Your password is: {password}")