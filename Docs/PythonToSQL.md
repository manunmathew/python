# Data Types
## String Data Types
CHAR(size)  A FIXED length string
VARCHAR(size) A VARIABLE length string
ENUM(val1, val2, val3, ...)	A string object that can have only one value, chosen from a list of possible values.

## Numeric Data Types
INT(size)	A medium integer.


## Date and Time Data Types
DATETIME(fsp)	A date and time combination

## create database
```sql
create database database_name;
```
## table creation
```sql
create table table_name(id int AUTO_INCREMENT ,name varchar, phone bigint, primary key(id));
```
## data insertion
```sql
insert into student_details(name) values('akshay');
```
## Questions
### what is database?
A database is an organized collection of data, so that it can be easily accessed and managed.
### what is mysql
MySQL is an open source RDBMS that uses SQL to create and manage databases.
### what is sql?
SQL stands for Structured Query Language.
SQL is a standard language for accessing and manipulating databases.
### what is rdbms
RDBMS stands for Relational Database Management System.
A relational database is a type of database. It uses a structure that allows us to identify and access data in relation to another piece of data in the database. Often, data in a relational database is organized into tables.
### what is char
The CHAR data type is a fixed-length data type
### varchar
A VARIABLE length string
### primary key
The PRIMARY KEY constraint uniquely identifies each record in a table.


###
Create a database Employee_management
create a table Employee_details with field
id Emp_name, salary, Designation, Email, company_name
insert 3 employee details
## select queries

select * from table_name

select Emp_name,Email,Designation from table_name

select * from table_name where id = 1
select * from Employee_details order by Emp_name; # assending
select * from Employee_details order by Emp_name desc;  # descenting




drop database databasename
drop table table_name
truncate table table_na,e
reanme table old_name to new_name


### what is foreign key
Foreign key is a column in a table that reference another a primary key in another table. it is used to link tables together


