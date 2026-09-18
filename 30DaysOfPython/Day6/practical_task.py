import time
while True:
    action = input(
        """
===MENU====
1. New Game
2. Play
3. Pause
4. Quit
-----------
"""
    )

    if action == "1":
        time.sleep(0.5)
        print("New game | Round 1 fight")
        time.sleep(0.5)

    elif action == "2":
        time.sleep(0.5)
        print("Continue your session...")
        time.sleep(0.5)

    elif action == "3":
        time.sleep(0.5)
        print("Game paused!")
        time.sleep(0.5)

    elif action == "4":
        time.sleep(0.5)
        print("|Good Bye! Thanks for playing")
        time.sleep(0.5)
        break
    else:
        time.sleep(0.5)
        print("Invalid input, input 1,2,3 or 4")