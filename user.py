def user_menu(username):
    print(f"Welcome, {username}!\n")
    print("""
1. Show courses
2. Buy course
3. Send message to teacher
4. Logout
""")
    while True:
        choice = input("Select: ")
        if choice == "1":
            print("Courses shown...")
        elif choice == "2":
            print("Course buying simulation...")
        elif choice == "3":
            print("Messaging...")
        elif choice == "4":
            print("Logged out.")
            break
        else:
            print("Invalid.")
