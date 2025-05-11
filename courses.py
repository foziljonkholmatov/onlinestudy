from file_manager import write,read ,current_time,generate_id

def add_course():
    name = input("Enter course name: ")
    price = input("Enter course price: ")
    courses = read("courses.csv")
    course_id = generate_id(courses)
    write("courses.csv", [course_id, name, price, current_time()])
    print("Course added successfully!")


def list_courses():
    courses = read("courses.csv")
    if not courses:
        print("No courses available!")
    print("Available courses: ")
    for course in courses:
        print(f"ID: {course[0]}, Name: {course[1]}, Price: {course[2]}")

