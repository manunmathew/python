import mysql.connector

db = mysql.connector.connect(host = "localhost", user = "root", password = "password@123", database = "luminar")
mycursor = db.cursor()

name = input("Enter the name of student: ")
qualification = input(f"Enter the qualification of {name}: ")
fee = int(input(f"Enter the fee for {name}: "))
email = input(f"Enter the email of {name}: ")
sql = f"insert into luminar_students(student_name, qualification, fee, email) values('{name}','{qualification}',{fee},'{email}')"

mycursor.execute(sql)
db.commit()
print(f"{name}'s details inserted")
