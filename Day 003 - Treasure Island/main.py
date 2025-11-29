print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________.|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=___________|___________________|___________________
|                   |  |  😎  |  |                   |
|   Welcome to      |  | Treasure |  |    Island!      |
|___________________|  |_________|  |___________________|
          |    ,-"_,=""     `"=.    |                  |
          |__"=___________|___________________|___________________
          |___________________|___________________|___________________
                    |  ,-"_,=""     `"=.    |                  |
                    |__"=___________|___________________|___________________
*******************************************************************************
''')

print("Welcome to Treasure Island!")
print("Your missions is to find the legendary treasure of Captain Blackbeard.\n")

print("You're standing at a sandy beach. Waves crash behind you.")
choice1 = input("The jungle path splits left and right. Do you go 'left' or 'right'? ").strip().lower()

if choice1 == "left":
    print("\nYou push through thick vines and reach a misty lake.")
    choice2 = input("There's an old boat and a rickety bridge. Do you 'wait' for the boat or 'cross' the bridge? ").strip().lower()

    if choice2 == "wait":
        print("\nA mysterious boatman rows you safely across. On the other side stands a ruined temple with three ancient doors: Red, Blue, and Yellow.")
        choice3 = input("Which door do you open? ('red', 'blue', or 'yellow')? ").strip().lower()

        if choice3 == "yellow":
            print("\nThe yellow door creaks open... GOLD EVERYWHERE!")
            print("You found Captain Blackbeard's legendary treasure!")
            print("YOU WIN!")
        elif choice3 == "red":
            print("\nFlames burst out! The door was cursed with eternal fire!")
            print("Game Over!")
        elif choice3 == "blue":
            print("\nA pack of ghostly pirates drags you into the underworld!")
            print("Game over!")
        else:
            print("\nYou stare at the doors too long... a trapdoor opens and you fall into spikes.")
            print("Game Over!")
    else:
        print("\nThe bridge collapses under your weight! You fall into crocodile-infested waters!")
        print("Game Over!")
else:
    print("\nYou walk straight into a trap! Poisonous darts fly from the trees!")
    print("Game Over.")