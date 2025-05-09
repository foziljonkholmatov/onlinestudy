from auth import register, login
from user import user_menu
print("""
Welcome to online study!
Menu:

1.Registration.
2.Login. 
3.Exit
""")
def main():
        while True:
            choice = input("Enter your choice: ")
            if choice == '1':
                register()
            elif choice == '2':
                user = login()
                if user:
                    user_menu(user)
            elif choice == '3':
                print("Good Bye!")
                break
            else:
                print("Invalid choice try again: ")
                continue

def teacher_menu():
    print("""Welcome to teacher's menu!\n
    Menu:\n
    1.Add course.
    2.Changing the cost of courses.
    3.Show messages.
    4.Show.
    5.who buy courses see received.
    6.Exit.
    """)
    while True:
        choice = input("Enter your choice: ")
        if choice == '1':
            pass
        elif choice == '2':
            pass
        elif choice == '3':
            pass
        elif choice == '4':
            pass
        elif choice == '5':
            pass
        elif choice == '6':
            print("Good Bye")
            break
        else:
            print("Invalid choice try again: ")
            continue


if __name__ == "__main__":
    main()