# WAP with class Employee that keeps a track of the number of employees in an organisation and also stores their name, designation, and salary details.

class Employee:
    global count_of_emp
    count_of_emp = 0

    def __init__(self):
        self.emp = {}
    def enterEmployeeDetails(self):
        i = int(input("Enter Employee id: "))
        n = input("Enter Employee Name: ")
        d = input("Enter Employee Designation: ")
        s = input("Enter Employee Salary: ")
        self.emp.update({str(i): [n, d, s]})
    def displayCount(self):
        print("Total count of employees: ", count_of_emp)
    def displayDetails(self):
        print("List of Employees and their details: ", self.emp)

e1 = Employee()
e1.enterEmployeeDetails()
count_of_emp += 1

e2 = Employee()
e2.enterEmployeeDetails()
count_of_emp += 1

e1.displayDetails()
e2.displayDetails()

e2.displayCount()
