import mysql.connector
db = mysql.connector.connect(host = "localhost", user = "root", password = "password@123", database = "luminar")
mycursor = db.cursor()
qualification = input("Enter the Qualification: ")
sql = f"select * from luminar_students where qualification = '{qualification}'"
# sql = "select * from luminar_students where fee = (select min(fee) from luminar_students)"
mycursor.execute(sql)
#data = mycursor.fetchone()
data = mycursor.fetchall()
print(data)

# btech
# min fee
# max fee
# order by
#limit clause
#between
