# 4. Write a program that has a class person. 
# Inherit a class Faculty from a person which 
# also has class Publications.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Faculty(Person):
    def __init__(self, name, age, designation):
        super().__init__(name, age)
        self.designation = designation
        self.publications = []

    def add_publication(self, publication):
        self.publications.append(publication)

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}, Designation: {self.designation}")
        print("Publications:", ", ".join(self.publications))

# Example usage
faculty = Faculty("Dr. John", 45, "Professor")
faculty.add_publication("AI Research")
faculty.add_publication("ML Fundamentals")
faculty.display()
