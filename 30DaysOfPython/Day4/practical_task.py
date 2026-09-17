print("""
====MENU====
1. Register
2. Log in
3. Log out
____________
""")
username = "yini-19"
password = "yaks591"

def verify_credentials():
    name_credential = input("input username: ")

    if name_credential != username:
        print("incorrect username")
        return
    elif name_credential == "":
        print("empty input not allowed")
        return

    else:
        print(f"{username}, input your passsword")
    
    pass_credential = input("input password: ")

    if pass_credential != password:
        print("Invalid credentials, try again")
        return
    elif pass_credential == "":
        print("empty input not allowed, input password")
        return

    else:
        print(f"Welcome {username}, login successful")

    

option = input("Select option: ")
if option == "1":
    print("Registration successful!")
elif option == "2":
    print(verify_credentials())
elif option == "3":
    print("Logged out! see you next time")
else:
    print("invalid input numbers 1, 2 or 3")



