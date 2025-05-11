from auth import register_user, register_teacher, login_user, login_teacher
from user import user_menu
from teacher import teacher_menu

def main():
    while True:
        print("""
Welcome to Online Study!
1. Register as User
2. Register as Teacher
3. Login as User
4. Login as Teacher
5. Exit
""")
        choice = input("Choice: ")
        if choice == "1":
            register_user()
        elif choice == "2":
            register_teacher()
        elif choice == "3":
            user = login_user()
            if user:
                user_menu(user)
        elif choice == "4":
            teacher = login_teacher()
            if teacher:
                teacher_menu(teacher)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid.")

if __name__ == "__main__":
    main()
