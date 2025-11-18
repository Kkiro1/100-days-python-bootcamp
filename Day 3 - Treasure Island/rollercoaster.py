print("Welcome to the rollercoaster!")

height = float(input("What is your height in cm? "))
if height >= 120:
    print("You can ride the rollercoaster")

    age = int(input("What is your age? "))
    bill = 0
    if age <= 12:
        bill = 5
        print("Child tickets are $5.")
    elif age <= 18:
        bill = 7
        print("Youth tickets are $7.")
    elif 45 <= age <= 55:
        print("Everything is going to be ok. Have a free ride on us :)")
    else:
        bill = 12
        print("Adults tickets are $12.")

    wants_photo = input("Do you want to have a photo take? (yes/no): ").strip().lower()
    if wants_photo in ["y", "yes"]:
        bill += 3

    print(f"Your final bill is ${bill}")
else:
    print("Sorry, you have to grow taller before riding it.")
