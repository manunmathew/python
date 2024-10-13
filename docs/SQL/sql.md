# SQL Notes

This document provides a detailed overview of fundamental SQL operations, including creating databases and tables, inserting data, querying records, and using various SQL clauses and functions.

---

## 1. Database Creation

### Description:
A database is a collection of related data. In SQL, you can create a new database using the `CREATE DATABASE` command.

### Syntax:
```sql
CREATE DATABASE database_name;
USE database_name;
```

### Example:
```sql
CREATE DATABASE Library_management;
USE Library_management;"
```
---

## 2. Table Creation

### Description:
A table is where data is stored in a structured format using rows and columns. You define tables with specific columns and data types using the `CREATE TABLE` command. You can also set primary keys and foreign keys to maintain referential integrity between related tables.

### Syntax:
```sql
CREATE TABLE table_name (
    column1 datatype constraints,
    column2 datatype constraints,
    ...
    PRIMARY KEY(column_name)
);
```

### Example:

Creating the `Employee_details` table:
```sql
CREATE TABLE Employee_details (
    id INT AUTO_INCREMENT PRIMARY KEY,
    Emp_name VARCHAR(30),
    salary INT,
    Designation VARCHAR(30),
    Email VARCHAR(50),
    company_name VARCHAR(30)
);
```

---

## 3. Using Foreign Keys

### Description:
A `FOREIGN KEY` in one table points to the `PRIMARY KEY` in another table, establishing a relationship between the two tables. Foreign keys are used to maintain referential integrity between tables by ensuring that data remains consistent.

### Syntax:
```sql
CREATE TABLE table_name (
    column1 datatype constraints,
    column2 datatype constraints,
    ...,
    FOREIGN KEY (column_name) REFERENCES referenced_table(referenced_column)
);
```

### Example:
Creating a `loans` table with a foreign key relationship to the `books` table:
```sql
CREATE TABLE loans (
    loan_id INT PRIMARY KEY,
    book_id INT,
    borrower_name VARCHAR(50),
    loan_date DATE,
    return_date DATE,
    FOREIGN KEY (book_id) REFERENCES books(book_id)
);
```

---

## 4. Inserting Data into a Table

### Description:
You can insert data into a table using the `INSERT INTO` statement. You can insert values either for all columns or specify certain columns.

### Syntax:
```sql
INSERT INTO table_name (column1, column2, ...)
VALUES (value1, value2, ...);
```

### Example:
```sql
INSERT INTO loans (loan_id, book_id, borrower_name, loan_date, return_date)
VALUES (1, 101, 'John Doe', '2024-10-01', '2024-10-15');
```

---

## 5. Retrieving Data (SELECT)

### Description:
The `SELECT` statement is used to query and retrieve data from a table. You can specify the columns to retrieve and filter data using various conditions.

### Syntax:
```sql
SELECT column1, column2, ...
FROM table_name
WHERE condition;
```

### Example:
- Retrieve all data from the `loans` table:
```sql
SELECT * FROM loans;
```
- Retrieve specific columns:
```sql
SELECT borrower_name, loan_date, return_date FROM loans;
```

---

## 6. Filtering Data (WHERE Clause)

### Description:
The `WHERE` clause is used to filter records based on a condition. It is commonly used with `SELECT`, `UPDATE`, and `DELETE` statements.

### Syntax:
```sql
SELECT * FROM table_name
WHERE condition;
```

### Example:
```sql
SELECT * FROM loans WHERE borrower_name = 'John Doe';
```

---

## 7. Logical Operators (AND, OR, NOT)

### Description:
Logical operators are used to combine multiple conditions in a `WHERE` clause.

- `AND`: All conditions must be true.
- `OR`: At least one condition must be true.
- `NOT`: Inverts the condition.

### Syntax:
```sql
SELECT * FROM table_name
WHERE condition1 AND/OR condition2;
```

### Example:
- Using `AND`:
```sql
SELECT * FROM loans WHERE borrower_name = 'John Doe' AND return_date = '2024-10-15';
```
- Using `OR`:
```sql
SELECT * FROM loans WHERE borrower_name = 'John Doe' OR return_date = '2024-10-15';
```
- Using `NOT`:
```sql
SELECT * FROM loans WHERE NOT loan_id = 1;
```
---

## 8. Ordering Data (ORDER BY)

### Description:
The `ORDER BY` clause is used to sort the result set in ascending (`ASC`) or descending (`DESC`) order based on one or more columns.

### Syntax:
```sql
SELECT * FROM table_name
ORDER BY column1 ASC|DESC;
```

### Example:
- Ascending order:
```sql
SELECT * FROM loans ORDER BY loan_date;
```

- Descending order:
```sql
SELECT * FROM loans ORDER BY loan_date DESC;
```

---

## 9. Aggregate Functions

### Description:
Aggregate functions perform calculations on a set of values and return a single value.

- **`MIN()`**: Returns the minimum value.
- **`MAX()`**: Returns the maximum value.
- **`AVG()`**: Returns the average value.

### Syntax:
```sql
SELECT MIN(column_name), MAX(column_name), AVG(column_name)
FROM table_name;
```
### Example:
- Minimum loan date:
```sql
SELECT MIN(loan_date) FROM loans;
```

- Maximum loan date:
```sql
SELECT MAX(loan_date) FROM loans;
```

- Average duration (hypothetically, if calculating durations):
```sql
SELECT AVG(DATEDIFF(return_date, loan_date)) FROM loans;
```

