# Exercise 1
temp = 50
if temp <= 30:
    print("Warning!, Low temperature!")
elif 30 < temp < 70:
    print("Warm temperature!")
else:
    print("Warning! Temperature is hot!")

# Exercise 2
age = 19
if age < 18:
    print("candidate is ineligible for this application")
else:
    print("candidate is eligible for this application")

# Exercise 3
print("""
====MENU====
1. Register
2. Log in
3. Log out
____________
""")
option = input("Select option: ")
if option == "1":
    print("Registration successful!")
elif option == "2":
    print("Login successful! Welcome")
elif option == "3":
    print("Logged out! see you next time")
else:
    print("invalid input numbers 1, 2 or 3")