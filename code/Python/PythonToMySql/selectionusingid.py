import mysql.connector
db = mysql.connector.connect(host = "localhost", user = "root", password = "password@123", database = "luminar")
mycursor = db.cursor()
id = int(input("Enter the ID: "))
sql = f"select * from luminar_students where id = {id}"
mycursor.execute(sql)
data = mycursor.fetchone()
print(data)
