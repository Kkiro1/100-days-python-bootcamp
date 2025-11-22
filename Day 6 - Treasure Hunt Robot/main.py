# =============================================
# Day 6 - Treasure Hunt Robot 🏴‍☠️💰
# Instead of Reeborg's World (can't share online)
# A text-based treasure hunt using only Day 6 skills!
# =============================================

import random

# ---------- CONFIG ----------
GRID_SIZE = 10
TREASURE_EMOJI = "💰"
ROBOT_EMOJI = "🤖"

# Hide the treasure at a random position
treasure_x = random.randint(0, GRID_SIZE - 1)
treasure_y = random.randint(0, GRID_SIZE - 1)

# Robot starts
robot_x = 0
robot_y = 0

# Calculate Manhattan distance (how "warm" or "cold")
def distance_to_treasure():
    return abs(robot_x - treasure_x) + abs(robot_y - treasure_y)

# First distance (so we can compare)
previous_distance = distance_to_treasure()

print("🏝️  Welcome to Treasure Island!")
print(f"You're {ROBOT_EMOJI} hunting for buried treasure {TREASURE_EMOJI} on a {GRID_SIZE}×{GRID_SIZE} island.")
print("I’ll tell you if you're getting warmer 🔥 or colder ❄️\n")

moves = 0

# Main game loop
while True:
    moves += 1
    print(f"Move #{moves} | Position: ({robot_x}, {robot_y})")

    # Show hint
    current_distance = distance_to_treasure()

    if current_distance == 0:
        print(f"🎉 YOU FOUND THE TREASURE {TREASURE_EMOJI} IN {moves} MOVES! 🎉")
        print("You're a true pirate legend! 🏴‍☠️\n")
        break
    elif current_distance < previous_distance:
        print("🔥 Getting warmer! You're closing in!")
    elif current_distance > previous_distance:
        print("❄️ Getting colder... wrong direction!")
    else:
        print("😐 Same temperature... try another way!")
        
    print("   (w = up, s = down, a = left, d = right)")
    
    # ASk player for direction
    direction = input("Which way do you want to go? (w/a/s/d): ").lower().strip()
    
    # Move the robot using functions!
    def move_up():
        global robot_y
        if robot_y < GRID_SIZE - 1:
            robot_y += 1
        else:
            print("🌊 You hit the ocean! Can't go further north.")
    
    def move_down():
        global robot_y
        if robot_y > 0:
            robot_y -= 1
        else:
            print("🌊 You hit the ocean! Can't go further south.")
    
    def move_left():
        global robot_x
        if robot_x > 0:
            robot_x -= 1
        else:
            print("🌊 You hit the ocean! Can't go further west.")
    
    def move_right():
        global robot_x
        if robot_x < GRID_SIZE - 1:
            robot_x += 1
        else:
            print("🌊 You hit the ocean! Can't go further east.")

    # Execute the chosen move
    if direction == "w":
        move_up()
    elif direction == "s":
        move_down()
    elif direction == "a":
        move_left()
    elif direction == "d":
        move_right()
    else:
        print("Invalid input! Use w, a, s, or d.")
        moves -= 1  # don't count invalid moves
        
    # Update distance for next turn
    previous_distance = current_distance
    print("-" * 40)

# Play again
while True:
    again = input("Want to hunt again? (y/n): ").lower()
    if again == "y" or again == "yes":
        # Reset everything and restart
        treasure_x = random.randint(0, GRID_SIZE - 1)
        treasure_y = random.randint(0, GRID_SIZE - 1)
        robot_x = 0
        robot_y = 0
        previous_distance = distance_to_treasure()
        moves = 0
        print("\n" + "="*50)
        print("NEW TREASURE HIDDEN! Starting again from (0,0)")
        print("="*50 + "\n")
        break
    elif any(x in again for x in ["n", "no"]):
        print("Thanks for playing! Happy coding!")
        exit()