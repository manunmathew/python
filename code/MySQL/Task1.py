# # create a database book_datas
# #Table book
# Book_id (primary key)
# title (Varchar)
# author (varchar)
# book_genre(varchar)
# pusblished (year)

# Table members
# member_id(primary key)
# Name (varchar)
# age(int)


# Task 1
# . list all book titles and their authors
# . retrieve the name of all members
# find all books of specific genere(eg: fiction)
# .get a total count of members (count())
# . list all books published year after 2000
import mysql.connector
def create_db(dbname):
    db = mysql.connector.connect(host = "localhost", user = "root", password = "password@123")
    mycursor = db.cursor()
    sql = f"create database {dbname}"
    mycursor.execute(sql)
    db.commit()

# create_db(dbname= "book_datas")

def create_table(dbname, table_name, *columns):
    db = mysql.connector.connect(host="localhost", user="root", password="password@123", database=dbname)
    mycursor = db.cursor()
    columns_definition = ", ".join(columns)
    sql = sql = f"CREATE TABLE {table_name} ({columns_definition})"
    mycursor.execute(sql)
    db.commit()
    print(f"table {table_name} created")

# create_table(
#     "book_datas",
#     "books",
#     "Book_id INT AUTO_INCREMENT PRIMARY KEY",
#     "title VARCHAR(100)",
#     "author VARCHAR(100)",
#     "book_genre VARCHAR(50)",
#     "published_year YEAR"
#     )

# create_table(
#     "book_datas",
#     "members",
#     "member_id INT AUTO_INCREMENT PRIMARY KEY",
#     "Name VARCHAR(100)",
#     "age INT"
# )

def insert_books(dbname, table_name, num_records):
    db = mysql.connector.connect(host="localhost", user="root", password="password@123", database=dbname)
    mycursor = db.cursor()
    for i in range(num_records):
        print(f"\nEnter details for book {i+1}:")
        title = input("Title: ")
        author = input("Author: ")
        published_year = input("Published Year: ")
        genre = input("Book genre: ")
        sql = f"insert into {table_name} (title, author, published_year, book_genre) VALUES ('{title}', '{author}', {published_year}, '{genre}')"
        mycursor.execute(sql)
        db.commit()
        print(f"Book {title} details entered")

num_books = int(input("How many books do you want to insert? "))
insert_books("book_datas", "books", num_books)

def insert_members(dbname, table_name, num_records):
    db = mysql.connector.connect(host="localhost", user="root", password="password@123", database=dbname)
    mycursor = db.cursor()
    for i in range(num_records):
        print(f"\nEnter details for member {i+1}:")
        name = input("Name: ")
        age = input("Age: ")
        sql = f"INSERT INTO {table_name} (name, age) VALUES ('{name}', {age})"
        mycursor.execute(sql)
        db.commit()
        print(f"Member {name}'s details entered")

# num_members = int(input("How many members do you want to insert? "))
# insert_members("book_datas", "members", num_members)

