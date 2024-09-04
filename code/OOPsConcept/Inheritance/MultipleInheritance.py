# create a class School
# school_details(School_Name, location)
# school_display
# create a class Parent
# parent_details (Parent_Name, address)
# parent_display

# Class Student
# student_details(Roll_No, Name, Department)
# student_display()
# view complete_details
# 2 student objects
# class School:
#     def school_details(self,School_Name, location):
#         self.School_Name = School_Name
#         self.location = location
#     def school_display(self):
#         print("School Name: ", self.School_Name)
#         print("School Location: ", self.location)
# class Parent:
#     def parent_details (self,Parent_Name, address):
#         self.Parent_Name = Parent_Name
#         self.address = address
#     def parent_display(self):
#         print("Parent Name: ", self.Parent_Name)
#         print("Parent Address: ", self.address)
# class Student(School,Parent):
#     def student_details(self,Roll_No, Name, Department):
#         self.Roll_No = Roll_No
#         self.Name = Name
#         self.Department = Department
#     def student_display(self):
#         print("Student Roll No: ", self.Roll_No)
#         print("Student Name: ", self.Name)
#         print("Student Department: ", self.Department)
#     def complete_details(self):
#         self.school_display()
#         self.parent_display()
#         self.student_display()

# student1 = Student()
# student1.school_details("ABC High School", "Pathanamthitta")
# student1.parent_details("NG Mathew", "Nampoodiathu")
# student1.student_details(1, "Manu Mathew", "Computer Science")

# student2 = Student()
# student2.school_details("XYZ High School", "Eranakulam")
# student2.parent_details("NG Mathew", "Nampoodiathu")
# student2.student_details(2, "Mithra Mathew", "Mathematics")

# print("Student 1 Details:")
# student1.complete_details()
# print()
# print("Student 2 Details:")
# student2.complete_details()


# class company , CompanyName, location
# teamleader ..team leader_name, department
# worker, emp_name, designation, salary


class Company:
    def __init__(self,CompanyName, location):
        self.CompanyName = CompanyName
        self.location = location
    def CompanyDisplay(self):
        print("Company Name: ", self.CompanyName)
        print("Company Location: ", self.location)
class Teamleader:
    def __init__(self,teamleader_name, department):
        self.TeamleaderName = teamleader_name
        self.department = department
    def TeamleaderDisplay(self):
        print("Teamleader Name: ", self.TeamleaderName)
        print("Department: ", self.department)
class Worker(Company,Teamleader):
    def __init__(self,CompanyName,location,teamleader_name,department,emp_name, designation, salary):
        Company.__init__(self,CompanyName, location)
        Teamleader.__init__(self,teamleader_name, department)
        self.emp_name = emp_name
        self.designation = designation
        self.salary = salary
    def WorkerDisplay(self):
        print("Employee Name: ", self.emp_name)
        print("Designation: ", self.designation)
        print("Salary: ", self.salary)
    def complete_details(self):
        self.CompanyDisplay()
        self.TeamleaderDisplay()
        self.WorkerDisplay()
worker1 = Worker("Orange Business", "Norway", "Manu Mathew", "Public Cloud", "Manu Mathew", "Software Developer", 85000)

print("Worker 1 Details:")
worker1.complete_details()
