import mysql.connector

db = mysql.connector.connect(host = "localhost", user="root", password = "password@123")
mycursor = db.cursor()

sql = "create database luminar"
mycursor.execute(sql)
db.commit()
print("Database created successfully...")
