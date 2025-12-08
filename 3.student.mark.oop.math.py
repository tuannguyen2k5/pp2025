import math
import numpy as np

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
        self.credit = 0
    def input(self):
        self.name = input("Enter course name: ")
        self.id = input("Enter course ID: ")
        self.credit = int(input("Enter course credit: "))
    def display(self):
        print(f"\nCourse name: {self.name}\nCourse ID: {self.id}\nCourse Credit: {self.credit}")

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
        course_id = input("Choose the Course ID to input mark: ")
        print("\n==========================")
        print("\nINPUT MARKS FOR STUDENT.")
        for s in self.students:
            mark_value = float(input(f"Mark for {s.name}: "))
            rounded_mark = math.floor(mark_value *10)/10

            m = Mark()
            m.student_name = s.name
            m.student_id = s.id
            m.course_id = course_id
            m.mark = rounded_mark

            self.marks.append(m)
    def displayMarks(self):
        COURSE_ID = input("\nEnter course ID to show mark: ")
        print(f"\n=== MARKS FOR COURSE {COURSE_ID} ===")
        for m in self.marks:
            if m.course_id == COURSE_ID:
                m.display()

    def getCourseCredit(self, course_id):
        for c in self.courses:
            if c.id == course_id:
                return c.credit
        print(f"Warning: Cannot find Credit for Course ID '{course_id}'. Defaulting to 0.")
        return 0
    def calculateGPA(self, student_id):
        student_marks = []
        student_credits = []

        for m in self.marks:
            if m.student_id == student_id:
                student_marks.append(float(m.mark))
                student_credits.append(self.getCourseCredit(m.course_id))

        if len(student_marks) == 0:
            return 0.0

        marks = np.array(student_marks)
        credits = np.array(student_credits)
        
        total_credits = np.sum(credits)
        
        # Kiểm tra tổng tín chỉ = 0 để tránh lỗi chia cho 0
        if total_credits == 0:
            return 0.0

        gpa = np.sum(marks * credits) / total_credits
        return round(gpa, 2)
    

    def showGPA(self):
        sid = input("Enter student ID to calculate GPA: ")
        gpa = self.calculateGPA(sid)
        print(f"\nGPA of student {sid} = {gpa}\n")
    def sortByGPA(self):
        print("\n==== SORTED STUDENT LIST BY GPA (DESCENDING) ====\n")

        # tạo danh sách (student, GPA)
        gpa_list = []
        for s in self.students:
            gpa = self.calculateGPA(s.id)
            gpa_list.append((s, gpa))

        # sắp xếp giảm dần
        gpa_list.sort(key=lambda x: x[1], reverse=True)

        for s, gpa in gpa_list:
            print(f"{s.name} (ID:{s.id}) - GPA: {gpa}")

management = Management()

management.inputStudent()
management.displayStudent()

management.inputCourse()
management.displayCourse()

management.inputMark()
management.displayMarks()

management.showGPA()
management.sortByGPA()