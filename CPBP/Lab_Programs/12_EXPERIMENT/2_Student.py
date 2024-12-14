# WAP that has classes such as Student, Course, Department. Enroll a student in a course of a particular department. Classes are - 
# Student details - name, roll no
# Course -  name, code, year and semester
# Department - Name

# Base class: Person
class Person:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Name: {self.name}"


# Student class inheriting from Person
class Student(Person):
    def __init__(self, name, roll_no):
        super().__init__(name)
        self.roll_no = roll_no

    def __str__(self):
        return f"Student Name: {self.name}, Roll No: {self.roll_no}"


# Base class: AcademicEntity
class AcademicEntity:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"{self.__class__.__name__} Name: {self.name}"


# Course class inheriting from AcademicEntity
class Course(AcademicEntity):
    def __init__(self, name, code, year, semester):
        super().__init__(name)
        self.code = code
        self.year = year
        self.semester = semester

    def __str__(self):
        return f"Course Name: {self.name}, Code: {self.code}, Year: {self.year}, Semester: {self.semester}"


# Department class inheriting from AcademicEntity
class Department(AcademicEntity):
    def __init__(self, name):
        super().__init__(name)
        self.courses = []  # List of courses in the department

    def add_course(self, course):
        self.courses.append(course)

    def __str__(self):
        return f"Department Name: {self.name}"


# Enrollment system for handling enrollments
class Enrollment:
    def __init__(self):
        self.enrollments = {}  # Maps students to courses

    def enroll_student(self, student, course, department):
        if student not in self.enrollments:
            self.enrollments[student] = []
        self.enrollments[student].append((course, department))

    def display_enrollments(self):
        for student, courses in self.enrollments.items():
            print(f"\n{student}:")
            for course, department in courses:
                print(f"  Enrolled in {course} of {department}")


# Main menu-driven program
if __name__ == "__main__":
    # Initialize data structures
    students = []
    courses = []
    departments = []
    enrollment_system = Enrollment()

    while True:
        print("\nMenu:")
        print("1. Add Department")
        print("2. Add Course")
        print("3. Add Student")
        print("4. Enroll Student in a Course")
        print("5. Display Enrollments")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            # Add a department
            dept_name = input("Enter department name: ")
            department = Department(dept_name)
            departments.append(department)
            print(f"Department '{dept_name}' added.")

        elif choice == "2":
            # Add a course
            if not departments:
                print("No departments available. Add a department first.")
                continue
            dept_name = input("Enter the department for the course: ")
            department = next((d for d in departments if d.name == dept_name), None)
            if not department:
                print("Department not found.")
                continue
            course_name = input("Enter course name: ")
            course_code = input("Enter course code: ")
            course_year = input("Enter course year: ")
            course_semester = input("Enter course semester: ")
            course = Course(course_name, course_code, course_year, course_semester)
            department.add_course(course)
            courses.append(course)
            print(f"Course '{course_name}' added to department '{dept_name}'.")

        elif choice == "3":
            # Add a student
            student_name = input("Enter student name: ")
            student_roll_no = input("Enter student roll number: ")
            student = Student(student_name, student_roll_no)
            students.append(student)
            print(f"Student '{student_name}' added.")

        elif choice == "4":
            # Enroll a student in a course
            if not students or not courses:
                print("No students or courses available. Add them first.")
                continue
            student_roll_no = input("Enter student roll number: ")
            student = next((s for s in students if s.roll_no == student_roll_no), None)
            if not student:
                print("Student not found.")
                continue
            course_code = input("Enter course code: ")
            course = next((c for c in courses if c.code == course_code), None)
            if not course:
                print("Course not found.")
                continue
            department = next((d for d in departments if course in d.courses), None)
            if not department:
                print("Department for the course not found.")
                continue
            enrollment_system.enroll_student(student, course, department)
            print(f"Student '{student.name}' enrolled in course '{course.name}'.")

        elif choice == "5":
            # Display all enrollments
            enrollment_system.display_enrollments()

        elif choice == "6":
            # Exit the program
            print("Exiting program. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")
