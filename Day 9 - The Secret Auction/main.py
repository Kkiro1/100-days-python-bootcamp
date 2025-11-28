import os
from art import logo

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

print(logo)
print("Welcome to the Secret Auction Program!")

bidders = {}
highest_bid = 0
winner = ""

while True:
    name = input("What's your name? ").strip()
    bid = float(input("What's your bid? $"))       
    bidders[name] = bid
    
    if bid > highest_bid:
        highest_bid = bid
        winner = name
        
    more_bidders = input("Are there more bidders? (yes/no): ").strip().lower()

    if more_bidders not in ["yes", "y"]:
        break
    
    clear_screen()

clear_screen()
print(f"\nThe highest bidder is {winner} with ${highest_bid:.2f}") 
    