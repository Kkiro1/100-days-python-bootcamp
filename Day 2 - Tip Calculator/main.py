print("Welcome to the Tip Calculator!")

total_bill = float(input("What was the total bill ? $"))
tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))

bill_per_person = (total_bill * (1 + tip / 100)) / people
print(f"Each person should pay: ${bill_per_person:.2f}")