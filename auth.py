from file_manager import read, write
from utils import send_email

def register():
    print("==== Registration ====")
    email = input("Enter Gmail address: ").strip().lower()

    if not email.endswith("@gmail.com"):
        print("Only Gmail is allowed.")
        return

    users = read("users.csv")
    for user in users:
        if email == user[0]:
            print("This email is already registered.")
            return

    password = input("Enter password: ")
    write("users.csv", [email, password])
    send_email(email, f"Hello!\nYou have successfully registered to Online Study.\nWelcome!", "Registration Successful")
    print("Registration completed and confirmation email sent.")

def login() -> str:
    print("==== Login ====")
    email = input("Enter Gmail: ").strip().lower()
    password = input("Enter password: ")
    users = read("users.csv")
    for user in users:
        if user[0] == email and user[1] == password:
            print("Login successful!")
            return email
    print("Invalid credentials.")
    return ""

def register():
    print("==== Registration ====")
    email = input("Enter Gmail address: ").strip().lower()

    if not email.endswith("@gmail.com"):
        print("Only Gmail is allowed.")
        return

    users = read("users.csv")
    for user in users:
        if email == user[0]:
            print("This email is already registered.")
            return

    password = input("Enter password: ")
    write("users.csv", [email, password])
    send_email(email, f"Hello!\nYou have successfully registered to Online Study.\nWelcome!", "Registration Successful")
    print("Registration completed and confirmation email sent.")

def login() -> str:
    print("==== Login ====")
    email = input("Enter Gmail: ").strip().lower()
    password = input("Enter password: ")
    users = read("users.csv")
    for user in users:
        if user[0] == email and user[1] == password:
            print("Login successful!")
            return email
    print("Invalid credentials.")
    return ""
