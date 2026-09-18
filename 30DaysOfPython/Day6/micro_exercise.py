#===Exercise 1===#
import time

for n in range(10, -1, -1):
    print(n)
    #time.sleep(1)

#===Exercise 2===#
while True:
    # 1. Ask for input INSIDE the loop so it updates every turn
    option = input("""
    ====MENU====
    1. Register
    2. Log in
    3. New Game
    4. Continue
    5. Quit
    ------------
               
Select option (1, 2, 3, 4, or 5): """)

    # 2. Process the options
    if option == "1":
        time.sleep(1)
        print("\n[!] Registration successful. You can now Log in.")
        time.sleep(2)
        # No need for 'continue' here; Python naturally loops back to the top
        
    elif option == "2":
        time.sleep(1)
        print("\n[!] Login successful. You can now start playing!")
        time.sleep(2)

    elif option == "3":
        time.sleep(1)
        print("\n[!] Welcome! | Round one. Fight! 🥊")
        time.sleep(2)

    elif option == "4":
        time.sleep(1)
        print("\n[!] Welcome back! Continuing your previous session...")
        time.sleep(2)

    elif option == "5":
        time.sleep(1)
        print("\n[!] Goodbye! Thanks for playing.")
        time.sleep(2)
        break  # Exits the loop and closes the program
        
    else:
        # Handles accidental typos (e.g., if the user types "6" or "hello")
        print("\n[X] Invalid option. Please type a number between 1 and 5.")
        time.sleep(1)

#===Exercise 3===#
count = 0
while count != 5:
    count += 1
print(count)