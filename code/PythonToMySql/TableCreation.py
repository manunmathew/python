import mysql.connector
db = mysql.connector.connect(host = "localhost", user = "root", password = "password@123", database = "luminar")
mycursor = db.cursor()
sql = "create table luminar_students(id int auto_increment primary key, student_name varchar(30), fee int, qualification varchar(20), email varchar(30))"
mycursor.execute(sql)
db.commit()
print("table created")
