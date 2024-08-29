# class Employees:
#     def employee_details(self,name,age,designation,salary,company_name):
#         self.name = name # public data
#         self.age = age
#         self.desig = designation
#         self.salary = salary
#         self.company = company_name
#     def emp_display(self):
#         print("Employee Name = ", self.name)
#         print("Age = ", self.age)
#         print("Designation = ", self.desig)
#         print("Salary = ", self.salary)
#         print("Company Name = ", self.company)
# emp1 = Employees()
# emp1.employee_details("Manu",40,"Developer",10000,"Orange")
# emp2 = Employees()
# emp2.employee_details("Arun",41,"Tester",15000,"TCS")

# emp1.emp_display()
# emp2.emp_display()

# Create a class Student with functions
# student_details(),
#stu_name, dept, roll, email, father_name, mother_name, address, school_name
# parent_details_display(),
#stu_name,father_name, mother_name, address,
# student_details_display
#stu_name, dept, roll, email,school_name
# create 2 student object
class Student:
    def student_details(self,stu_name,dept,roll,email,father_name, mother_name,address,school_name):
        self.name = stu_name
        self.dept = dept
        self.roll = roll
        self.email = email
        self.father = father_name
        self.mother = mother_name
        self.address = address
        self.school = school_name
    def parent_details_display(self):
        print("Student Name = ", self.name)
        print("Father Name = ", self.father)
        print("Mother Name = ", self.mother)
        print("Address = ", self.address)
    def student_details_display(self):
        print("Student Name = ", self.name)
        print("Department = ", self.dept)
        print("Roll Number = ", self.roll)
        print("Email Id = ", self.email)
        print("School Name = ", self.school)
stu1 = Student()
stu1.student_details("Manu","Maths","101","manu@123.com","N G Mathew","Kunjamma Mathew","Nampoodiathu","Charter")
stu2 = Student()
stu2.student_details("Mithra","Science","102","mithra@123.com","Manu Mathew","xyz zzz","Nampoodiathu","Charter")

stu1.parent_details_display()
stu2.parent_details_display()
stu1.student_details_display()
stu2.student_details_display()
