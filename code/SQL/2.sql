create database Employee_management;
use Employee_management;
create table Employee_details(id int auto_increment primary key, Emp_name varchar(30),salary int, Designation varchar(30), Email varchar(50), company_name varchar(30));
insert into Employee_details (Emp_name, salary, Designation, Email, company_name)
values 
('Manu Mathew', 50000.00, 'Software Engineer', 'manumathew@123.com', 'Tech Solutions'),
('Theja', 60000.00, 'Project Manager', 'teja@123.com', 'Tech Solutions'),
('Shilpa', 45000.00, 'Data Analyst', 'shilpa@123.com', 'Tech Solutions');
select * from Employee_details;
select Emp_name,Email,Designation from Employee_details;
select * from Employee_details where id = 1;
select * from Employee_details where Designation = 'Software Engineer';
select Emp_name,Email from Employee_details where id = 1;
select * from Employee_details where Emp_name = 'Manu Mathew' and Email = 'manumathew@123.com';
select * from Employee_details where Emp_name = 'Manu Mathew' or Email = 'teja@123.com';
select * from Employee_details where not id = 1;
select * from Employee_details order by Emp_name;
select * from Employee_details order by Emp_name desc;
select min(salary) from Employee_details;
select max(salary) from Employee_details;
select avg(salary) from Employee_details;
select * from Employee_details where salary = (select min(salary) from Employee_details);
select * from Employee_details where salary = (select max(salary) from Employee_details);


