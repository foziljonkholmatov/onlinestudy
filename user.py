from courses import list_courses
from purchase import buy_course, list_user_courses
from message import send_message

def user_menu(username):
    while True:
        print("""
1. Show all courses
2. Buy course
3. Show my courses
4. Send message to teacher
5. Logout
""")
        choice = input("Select: ")
        if choice == "1":
            list_courses()
        elif choice == "2":
            buy_course(username)
        elif choice == "3":
            list_user_courses(username)
        elif choice == "4":
            send_message()
        elif choice == "5":
            print("Logged out.")
            break
        else:
            print("Invalid.")
