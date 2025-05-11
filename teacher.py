from courses import add_course, list_courses
from message import show_messages

def teacher_menu(teacher_email):
    while True:
        print("""
1. Add course
2. Show courses
3. Show received messages
4. Logout
""")
        choice = input("Select: ")
        if choice == "1":
            add_course()
        elif choice == "2":
            list_courses()
        elif choice == "3":
            show_messages(teacher_email)
        elif choice == "4":
            print("Logged out.")
            break
        else:
            print("Invalid.")