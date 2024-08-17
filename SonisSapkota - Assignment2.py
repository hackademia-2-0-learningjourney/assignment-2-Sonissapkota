import json 

def sign_up():
    try:
        with open("user_data.json", "r") as file:
            users = json.load(file)
    except FileNotFoundError:
        users = []
    
    username = input("Enter a username: ")
    password = input("Enter a password: ")
    mobile_number = input("Enter your mobile number: ")
    
    user_data = {
        "username": username,
        "password": password,
        "mobile_number": mobile_number
    }
    users.append(user_data)
    with open("user_data.json", "w") as file:
        json.dump(users, file, indent=4)
    print("Sign up successful!")

def sign_in():
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    try:
        with open("user_data.json", "r") as file:
            users = json.load(file)
    except FileNotFoundError:
        users = []
    
    for user in users:
        if username == user["username"] and password == user["password"]:
            print(f"Welcome to the device! Your mobile number is {user['mobile_number']}.")
            return
    
    print("Wrong username or password. Please try again")


print("1. Sign up")
print("2. Sign in")
    
while True:
    choice = input("Enter 1 or 2: ")
    if choice == '1':
        sign_up()
    elif choice == '2':
        sign_in()
    else:
        print("Something error occured")
