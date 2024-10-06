create database library;
use library;
create table authors( author_id int primary key, name varchar(30));
insert into  authors(author_id,name) values(101, 'Thakazhi Sivasankara Pillai');
insert into authors(author_id, name) value(102, 'Benyamin');
insert into authors(author_id, name) value(103, 'Vaikom Muhammad Basheer');

create table books(book_id int primary key, title varchar(50), author_id int, genre varchar(30), published_year year, foreign key (author_id) references authors(author_id));
insert into books(book_id, title, author_id, genre, published_year) values (201, 'Chemmeen', 101, 'Romance', 1956);
insert into books(book_id, title, author_id, genre, published_year) values (202, 'Kayar', 101, 'Fiction', 1959);
insert into books(book_id, title, author_id, genre, published_year) values (210, 'Aadujeevitham', 102, 'Fiction', 2008);
insert into books(book_id, title, author_id, genre, published_year) values (220, 'Bharathapuzha', 103, 'Fiction', 1967);


create table loans(loan_id int primary key, book_id int, borrower_name varchar(50), loan_date date, return_date date, foreign key (book_id) references books(book_id));

insert into loans(loan_id, book_id, borrower_name, loan_date, return_date) 
values (301, 201, 'Manu Mathew', '2023-09-01', '2023-09-15');

insert into loans(loan_id, book_id, borrower_name, loan_date, return_date) 
values (302, 210, 'Mithra Sera', '2023-09-05', '2023-09-20');

insert into loans(loan_id, book_id, borrower_name, loan_date, return_date) 
values (303, 220, 'Reeba Mathew', '2023-09-10', '2023-09-25');
select * from loans;
select * from books;

-- retrive all book details along with author details
select books.title, authors.name, books.genre, books.published_year from books join authors on books.author_id = authors.author_id;