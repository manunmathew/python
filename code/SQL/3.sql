-- # create a database products
-- # create 2 tables
-- # product_details .. id, product_id, product_name, price, description
-- # customer_details .. id, customer_name, address, phone

-- # insert 5 data for each
-- # select product details
-- # select customer details
-- # select product_name and price of a product using product id
-- # select customer details using phone number
-- # select max price product details
-- # select customer details in ascending order using name



create database products;
use products;
create table product_details(id int auto_increment primary key, product_id int, product_name varchar(50), price int, description varchar(200));
create table customer_details(id int auto_increment primary key, customer_name varchar(50), address varchar(100), phone bigint);
insert into product_details(product_id, product_name, price,description)
values
(101, 'Laptop', 50000, 'High-end gaming laptop'),
(102, 'Smartphone', 15000, 'Latest smartphone model'),
(103, 'Tablet', 30000, 'Portable tablet'),
(104, 'Smartwatch', 10000, 'Fitness smartwatch'),
(105, 'Headphones', 7000, 'Noise-cancelling headphones');
insert into customer_details (customer_name, address, phone)
values
('Manu Mathew', 'Pathanamthitta', 9876543210),
('Mithra Sera', 'Pukkattupady', 8765432109),
('Albin Biju', 'Nariyapuram', 7654321098),
('Reba Mathew', 'Nariyapuram', 6543210987),
('Jubin Raju', 'Manjinikara', 5432109876);
select * from product_details;
select * from customer_details;
select product_name,price from product_details where product_id = 103;
select * from customer_details where phone = 9876543210;
select * from product_details where price = (select max(price) from product_details);
select * from customer_details order by customer_name;
