print("Welcome to the Dungeon Escape Adventure!")

print("\nYou wake up in a dark dungeon with two visible exits.")
print("1. Go through the rusty door.")
print("2. Crawl into the narrow tunnel.")

choice1 = input("What do you choose? (1 or 2): ")

if choice1 == "1":
    print("\nYou slowly open the rusty door and enter a dimly lit hallway.")
    print("At the end, you see a staircase going up and a trapdoor on the floor.")
    print("1. Climb the staircase.")
    print("2. Open the trapdoor.")
    
    choice2 = input("What do you choose? (1 or 2): ")
    
    if choice2 == "1":
        print("\nYou climb the stairs and find a guard asleep.")
        print("1. Sneak past him.")
        print("2. Try to fight him.")
        
        choice3 = input("What do you choose? (1 or 2): ")
        
        if choice3 == "1":
            print("\nYou sneak past the guard successfully and find the exit. You're free!")
        elif choice3 == "2":
            print("\nThe guard wakes up mid-fight and knocks you out. Game Over.")
        else:
            print("\nInvalid choice. You hesitate and get caught. Game Over.")

    elif choice2 == "2":
        print("\nYou open the trapdoor and fall into a pit of snakes. Oops. Game Over.")
    else:
        print("\nInvalid choice. The delay costs you your life. Game Over.")

elif choice1 == "2":
    print("\nYou crawl into the tunnel. It's tight and dark, but you manage.")
    print("After a while, you see light and a fork in the tunnel.")
    print("1. Go left toward the sound of water.")
    print("2. Go right toward the faint glow.")

    choice2 = input("What do you choose? (1 or 2): ")

    if choice2 == "1":
        print("\nYou find an underground river. You swim across and escape through a sewer grate. Freedom!")
    elif choice2 == "2":
        print("\nYou head toward the glow and find a torch-lit room… with a monster waiting. Game Over.")
    else:
        print("\nYou get lost in the tunnel and never make it out. Game Over.")

else:
    print("\nYou hesitate too long and a hidden trap activates. You're done. Game Over.")
