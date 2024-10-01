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
select * from customer_details limit 4;
select * from customer_details limit 2, 5;
select * from customer_details where id between 2 and 5;
select product_details.product_name, product_details.price, product_details.description, customer_details.customer_name, customer_details.address, customer_details.phone from product_details inner join customer_details on product_details.id = customer_details.id;
select * from product_details inner join customer_details on product_details.id = customer_details.id;
update product_details set price = 8000 where id = 5;
SET SQL_SAFE_UPDATES = 0;
update product_details set price = 9000 where id = 5 or product_name = 'Headphones';
alter table product_details add quantity int;
update product_details set quantity = 2 where id = 5;
update product_details set quantity = 3 where id = 4;
update product_details set quantity = 2 where id = 3;
update product_details set quantity = 5 where id = 2;
update product_details set quantity = 5 where id = 1;
alter table customer_details add(email varchar(50), pincode int);
alter table customer_details add phone2 bigint after phone;
alter table customer_details drop column phone2;
alter table customer_details drop column email, drop column pincode;
delete from customer_details where id = 4;