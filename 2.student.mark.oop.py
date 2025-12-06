class Student():
    def __init__(self):
        self.id = ""
        self.name = ""
        self.Dob = ""
    def input(self):
        self.name = input("Student Name: ")
        self.id = input("Student ID: ")
        self.Dob = input("Student Dob: ")
    def display(self):
        print(f"Student {self.name}\nID: {self.id}\nDOB: {self.Dob}")
class Course():
    def __init__(self):
        self.id = ""
        self.name = ""
    def input(self):
        self.name = input("Course Name: ")
        self.id = input("Course ID:")
    def display(self):
        print(f"Course: {self.name}\nID: {self.id}")
class Mark():
    def __init__(self):
        self.name = ""
        self.student_id = ""
        self.course_id = ""
        self.mark = ""
    def display(self):
        print(f"Student:{self.name}\nStudent ID:{self.student_id}\nCourse ID: {self.course_id},\nMark: {self.mark}")
class MarkManagement():
    def __init__(self):
        self.students = []
        self.courses = []
        self.marks = []
    def inputStudents(self):
        n = int(input("Enter the number students: "))
        for i in range(n):
            s = Student()
            s.input()
            self.students.append(s)
    def inputCourses(self):
        n = int(input("Enter the number courses: "))
        for i in range(n):
            c = Course()
            c.input()
            self.courses.append(c)
    def inputMarks(self):
        print("\nAvaiable courses: ")
        for c in self.courses:
            c.display()
        course_id = input("Select course ID to input marks: ")
        print("\n============")
        print("\nInput marks for students.")
        for s in self.students:
            mark_value = input(f"Mark for {s.name}:")
            m = Mark()
            m.student_id = s.id
            m.course_id = course_id
            m.mark = mark_value
            self.marks.append(m)
    
    # LIST FUNCTION
    def displayStudents(self):
        print("=== Student List ===")
        for s in self.students:
            s.display()
    def displayCourses(self):
        print("\n=== Course List ===")
        for c in self.courses:
            c.display()
    def showMarks(self):
        course_id = input("Enter course ID to show marks: ")
        print(f"\n=== Marks for course {course_id} ===")
        for m in self.marks:
            if m.course_id == course_id:
                print(f"{m.student_id}:{m.mark}")
        
Management = MarkManagement()
Management.inputStudents()
Management.inputCourses()
Management.inputMarks()
Management.displayStudents()
Management.displayCourses()
Management.showMarks()