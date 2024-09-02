# Create a parent class company with methods
    # company_info(company_name, location, CEO, company_email)
    # company_display ( all above)
  # create child class employee with methods
    # employee_info(emp_name, salary, phone, designation)
    # employee_display

# class Company:
#     def company_info(self,company_name, location, CEO, company_email):
#         self.company_name = company_name
#         self.location = location
#         self.CEO = CEO
#         self.company_email = company_email
#     def company_display(self):
#         print("Company Name ",self.company_name)
#         print("Location ",self.location)
#         print("CEO ",self.CEO)
#         print("Company Email",self.company_email)
# class Employee(Company):
#     def employee_info(self, emp_name, salary, phone, designation):
#         self.emp_name = emp_name
#         self.salary = salary
#         self.phone = phone
#         self.designation = designation
#     def employee_display(self):
#         print("Employee Name ",self.emp_name)
#         print("Salary ",self.salary)
#         print("Phone ",self.phone)
#         print("Designation",self.designation)
# emp = Employee()
# emp.company_info("Luminar Solutions", "Kakkanad", "Manu Mathew", "luminar@123.com")
# emp.employee_info("Theja", 90000, "12345678", "Software Engineer")
# emp.employee_display()



# class Company:
#     def __init__(self,company_name, location):
#         self.company_name = company_name
#         self.location = location

#     def company_display(self):
#         print("Company Name ",self.company_name)
#         print("Location ",self.location)

# class Employee(Company):
#     def __init__(self, company_name, location, emp_name, salary, phone):
#         super().__init__(company_name,location)
#         self.emp_name = emp_name
#         self.salary = salary
#         self.phone = phone

#     def employee_display(self):
#         self.company_display()
#         super().company_display()
#         print("Employee Name ",self.emp_name)
#         print("Salary ",self.salary)
#         print("Phone ",self.phone)

# emp = Employee("Luminar Solutions", "Kakkanad", "Theja", 90000, "12345678")
# emp.employee_display()
# emp.company_display()


# create a class Hospital using constructor method.
#arguments Hospital Name, Hospital_head, location
#hospital_display()

# create child class : patient
# id, name, doctor_name
# patient_display()
# complete_details()

class Hospital:
    def __init__(self,hospital_name, hospital_head, location):
        self.hospital_name = hospital_name
        self.hospital_head = hospital_head
        self.location = location
    def hospital_display(self):
        print("Hospital Name ", self.hospital_name)
        print("Hospital Head ", self.hospital_head)
        print("Location ", self.location)
class Patient(Hospital):
    def __init__(self,hospital_name, hospital_head, location,id,name,doctor_name):
        super().__init__(hospital_name, hospital_head, location)
        self.id = id
        self.name = name
        self.doctor_name = doctor_name
    def patient_display(self):
        print("Patient Name ", self.name)
        print("Patient Id ", self.id)
        print("Doctor Name ", self.doctor_name)
    def complete_details(self):
        super().hospital_display()
        self.patient_display()

patient1 = Patient("City Hospital", "Dr. John", "Kakkanad", 123, "Manu", "Dr. Mathew")
patient1.patient_display()
patient1.complete_details()
