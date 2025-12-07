class Student():
    def __init__(self):
        self.id = ""
        self.name = ""
        self.Dob = ""
    def input(self):
        self.name = input("Enter student name: ")
        self.id = input("Enter student ID: ")
        self.Dob = input("Enter student Dob: ")
    def display(self):
        print(f"\nStudent Name: {self.name}\nStudent ID: {self.id}\nStudent Dob: {self.Dob}")
class Course():
    def __init__(self):
        self.id = ""
        self.name = ""
    def input(self):
        self.name = input("Enter course name: ")
        self.id = input("Enter course ID: ")
    def display(self):
        print(f"\nCourse name: {self.name}\nCourse ID: {self.id}")
class Mark():
    def __init__(self):
        self.student_name = ""
        self.student_id = ""
        self.course_id = ""
        self.mark = ""
    def display(self):
        print(f"\nStudent name:{self.student_name} - ID:{self.student_id} - Course ID:{self.course_id} - Mark:{self.mark}")
class Management():
    def __init__(self):
        self.students = []
        self.courses = []
        self.marks = []
    def inputStudent(self):
        n = int(input("Enter number students: "))
        for i in range(n):
            s = Student()
            s.input()
            self.students.append(s)
    def displayStudent(self):
        print("\n==== LIST STUDENTS ====")
        for s in self.students:
            s.display()
    def inputCourse(self):
        n = int(input("Enter number courses: "))
        for i in range(n):
            c = Course()
            c.input()
            self.courses.append(c)
    def displayCourse(self):
        print(f"\n=== COURSE LIST ===")
        for c in self.courses:
            c.display()
    def inputMark(self):
        course_id = input("Choose the course to input mark: ")
        print("\n==========================")
        print("\nINPUT MARKS FOR STUDENT.")
        for s in self.students:
            mark_value = input(f"Mark for {s.name}: ")
            m = Mark()
            m.student_name = s.name
            m.student_id = s.id
            m.course_id = course_id
            m.mark = mark_value
            self.marks.append(m)
    def displayMarks(self):
        COURSE_ID = input("\nEnter course ID to show mark: ")
        print(f"\n=== MARKS FOR COURSE {COURSE_ID} ===")
        for m in self.marks:
            if m.course_id == COURSE_ID:
                m.display()
management = Management()
management.inputStudent()
management.displayStudent()
management.inputCourse()
management.displayCourse()
management.inputMark()
management.displayMarks()