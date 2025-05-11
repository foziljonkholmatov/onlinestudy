from file_manager import write, read, generate_id, current_time


def register_user():
    email = input("Enter mail: ")
    users = read("users.csv")
    for user in users:
        if len(user) >= 2 and user [1] == email:
            print("This mail is already registered!")
            return
    password = input("Enter password: ")

    user_id = generate_id(users)
    write("users.csv", [user_id, email, password, current_time()])
    print("User registered successfully!")


def register_teacher():
    email = input("Enter email: ")
    teachers = read("teachers.csv")
    for teach in teachers:
        if len(teach) >= 2 and teach[1] == email:
            print("This email is already registered.")
            return
    password = input("Enter password: ")

    teacher_id = generate_id(teachers)
    write("teachers.csv", [teacher_id, email, password, current_time()])
    print("Teacher registered successfully!")


def login_user():
    email = input("Enter email: ")
    password = input("Enter password: ")
    users = read("users.csv")
    for user in users:
        if user[1] == email and user[2] == password:
            print("Login successfully")
            return user[1]
    print("Invalid credentials.")
    return None


def login_teacher():
    email = input('Enter email: ')
    password = input("Enter password: ")
    teachers = read('teachers.csv')
    for teach in teachers:
        if len(teach) >= 3 and teach[1] == email and teach[2] == password:
            print("Login successfully!")
            return teach[1]
    print("Invalid credentials.")
    return None
