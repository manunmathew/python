use luminar;
select * from luminar_students;
insert into luminar_students(student_name, qualification, fee, email) values('Reeba','Btech',40000,'reeba@123.com');
insert into luminar_students(student_name, qualification, fee, email) values('Mithra','Mtech',60000,'mithra@123.com');

use book_datas;

alter table books drop column genre ;
SET SQL_SAFE_UPDATES = 0;
UPDATE books SET genre = 'Fiction' WHERE title = 'Kayar';
UPDATE books SET genre = 'Fiction' WHERE title = 'Aadujeevitham';
update books set genre = 'Satire' where title = 'Nireeswaran';

select * from books;

