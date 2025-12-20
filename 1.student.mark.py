students = []
courses = []
marks = {} #{course_id: {student_id: mark}}

# STUDENTS
def information_student():
    student_name = input("Enter the student name: ")
    student_id = input("enter the student id: ")
    

    for s in students:
        if s["id"] == student_id:
            print("Student ID already exists! Please re-enter.")
            return information_student()
        
    student_Dob = input("enter date of birth: ")
    
    students.append({
        "id" : student_id, 
        "name": student_name, 
        "Dob": student_Dob
    })
def input_student():
    n = int(input("enter the number of students in a class: "))
    while n < 1:
        print(f"Invalid number of students!!")
        n = int(input("enter the number of students in a class: "))
    
    for i in range(n):
        print(f"\n--- Student {i+1} ---")
        information_student()
    print("\nStudent input successfully!!")
    return n
# =========
#COURSE
def information_course():
    course_name = input("enter course name: ")
    course_id = input("enter course ID: ")

    for c in courses:
        if c["id"] == course_id:
            print("Course ID already exists! Please re-enter.")
            return information_course()
        
    courses.append({
        "id": course_id,
        "name": course_name
    })
def input_course():
    n = int(input("\nEnter number of the courses: "))
    while n<1:
        print(f"Invalid number of courses!!")
        n = int(input("\nEnter number of the courses: "))
    
    for i in range(n):
        print(f"\n--- course {i+1} ---")
        information_course()
    print("\nCourses input successfully!!")
    return n

# Marks

def input_marks():
    if not students:
        print("No students available!")
        return
    if not courses:
        print("No courses available!")
        return
    print("\nAvailable courses: ")
    for i, c in enumerate(courses): # vòng lặp for sử dụng enumerate()
        print(f"{i+1}.{c['name']} (ID: {c['id']})")

    choice = int(input("\nSelect a course by number: ")) - 1
    if choice <0 or choice >= len(courses):
        print("Invalid course selection!")
        return
    course_id = courses[choice]["id"]
    """
    courses là list các dictionary
    courses[choice] lấy ra 1 dictionary
    ["id"] truy cập vào key “id”
    """
    marks[course_id] = {}

    print(f"\nEnter marks for course: {courses[choice]['name']}")
    for s in students:
        while True:
            score = float(input(f"Enter mark for {s['name']} (ID: {s['id']}): "))
            if 0<= score <=20:
                break
            print("Invalid mark! Enter a value between 0 and 20.")
        marks[course_id][s["id"]]= score
    print("\nMarks input successfully!")

# Listing functions
def list_students():
    print("\n=== STUDENT LIST ===")
    for s in students:
        print(f"ID: {s['id']}, Name: {s['name']}, DOB: {s['Dob']}")

def list_courses():
    print("\n=== COURSE LIST ===")
    for c in courses:
        print(f"ID: {c['id']}, Name: {c['name']}")
def show_marks():
    print("\nAvaiable courses:")
    for i, c in enumerate(courses):
        print(f"{i+1}. {c['name']} (ID: {c['id']})")

    choice = int(input("\nSelect a course to view marks: ")) - 1
    if choice <0 or choice >= len(courses):
        print("Invalid course selection!")
        return
    course_id = courses[choice]["id"]

    print(f"\n=== Marks for course: {courses[choice]['name']} ===")

    if course_id not in marks:
        print("No marks recorded for this course.")
        return
    for s in students:
        s_id = s["id"]
        score = marks[course_id].get(s_id, "N/A")
        print(f"{s['name']} ({s_id}): {score}")

def main():
    input_student()
    input_course()
    input_marks()
    list_students()
    list_courses()
    show_marks()

main()   