from file_manager import read, write, current_time, generate_id

def buy_course(username):
    course_id = input("Enter course ID to buy: ")
    purchases = read('purchases.csv')
    purchase_id = generate_id(purchases)
    write('purchases.csv', [purchase_id, username, course_id, current_time()])
    print('Course purchased successfully!')

def list_user_courses(username):
    purchases = read('purchases.csv')
    courses = read('courses.csv')
    user_courses = [p[2]for p in purchases if p[1] == username]
    if not user_courses:
        print("You have not purchased any courses.")
        return
    for course in courses:

        if course[0] in user_courses:
            print(f"ID: {course[0]}, Name: {course[1]}")


