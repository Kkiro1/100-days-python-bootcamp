print("Welcome to Python Pizza Deliveries!")

size = input("What pizza size do you want? S, M or L: ").strip().lower()
pepperoni = input("Do you want pepperoni on your pizza? (y/n)? ").strip().lower()
extra_cheese = input("Do you want extra cheese? (y/n)? ").strip().lower()

bill = 0
if size == "s":
    bill = 15
elif size == "m":
    bill = 20
elif size == "l":
    bill = 25
else:
    print("Invalid choice.")

if pepperoni == "y":
    if size == "s":
        bill += 2
    else:
        bill += 3

if extra_cheese == "y":
    bill += 1

print(f"Your final bill is ${bill}")