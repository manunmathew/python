# create a class BasicData
        #using constructor (Name, Gender, qualification, phone)
# class Doctor
    #using constructor (specialization, hospital_name)
        # doctor_display()
# class Engineer
    # constructor(company_name, it_department)
# class Teacher
    # school_name, department

class BasicData:
    def __init__(self,Name, Gender, Qualification, Phone):
        self.Name = Name
        self.Gender = Gender
        self.Qualification = Qualification
        self.Phone = Phone
    def BasicData_display(self,):
        print(f"Name: {self.Name} \nGender: {self.Gender} \nQualification: {self.Qualification} \nPhone: {self.Phone}")
class Doctor(BasicData):
    def __init__(self,Name, Gender, Qualification, Phone,Specialization, Hospital_name):
        super().__init__(Name, Gender, Qualification, Phone)
        self.Specialization = Specialization
        self.Hospital = Hospital_name
    def doctor_display(self,):
        self.BasicData_display()
        print(f"Specialization: {self.Specialization} \nHospital Name: {self.Hospital} ")
class Engineer(BasicData):
    def __init__(self,Name, Gender, Qualification, Phone, Company_name, It_department):
        super().__init__(Name, Gender, Qualification, Phone)
        self.Company_name = Company_name
        self.It_department = It_department
    def Engineer_display(self,):
        self.BasicData_display()
        print(f"Company Name: {self.Company_name} \nIt_department: {self.It_department}")
class Teacher(BasicData):
    def __init__(self,Name, Gender, Qualification, Phone, School_name, Department):
        super().__init__(Name, Gender, Qualification, Phone)
        self.School_name = School_name
        self.Department = Department
    def Teacher_display(self,):
        self.BasicData_display()
        print(f"School Name: {self.School_name} \nDepartment: {self.Department}")
doctor = Doctor("Manu Mathew", "Male", "MBBS", "1234567890", "Cardiology", "City Hospital")
engineer = Engineer("Mithra Mathew", "Female", "B.Tech", "0987654321", "Tech Corp", "Software")
teacher = Teacher("Reji Mathew", "Male", "M.Ed", "1122334455", "Sunrise School", "Math")
print("===Doctor Details===")
doctor.doctor_display()
print("===Engineer Details===")
engineer.Engineer_display()
print("===Teacher Details===")
teacher.Teacher_display()
