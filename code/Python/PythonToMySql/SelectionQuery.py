import mysql.connector
db = mysql.connector.connect(host = "localhost", user = "root", password = "password@123", database = "luminar")
mycursor = db.cursor()
sql = "select * from luminar_students"
mycursor.execute(sql)
# fetchall(): it is a method that is used to fetch all raws of a query an returns a list of tuples
data = mycursor.fetchall()
print(data)
