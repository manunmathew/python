# Django Models and ORM (Object-Relational Mapping)

## Introduction

Django models serve as the interface to your database, allowing you to create, retrieve, update, and delete records using Django's Object-Relational Mapper (ORM). The ORM handles database operations behind the scenes, allowing developers to work with Python code instead of writing raw SQL queries.

## Key Concepts

- **ORM (Object-Relational Mapper)**: A way for Django to interact with a database without writing SQL. Using ORM, developers define models as Python classes, which Django translates to database tables.
- **CRUD Operations**: Refers to the basic operations to Create, Read, Update, and Delete records in the database.

## Defining a Model

In Django, you define database tables by creating model classes. Each model maps to a single table in the database, and each model attribute represents a table field.

### Example SQL Table

Here’s an example SQL query for creating a table:

```sql
CREATE TABLE Add (
    num1 INT,
    num2 INT,
    answer INT
);
```

### Django Model Representation

The above table can be represented in Django as follows:

```python
from django.db import models

class Add(models.Model):
    num1 = models.IntegerField()
    num2 = models.IntegerField()
    answer = models.IntegerField()
```

In this example:
- Each field corresponds to a column in the database table.
- `IntegerField` is used to store integer values.

## CRUD Operations Using Django ORM

### 1. Create a Record

To insert a record in the `Add` table:

```python
Add.objects.create(num1=5, num2=3, answer=8)
```

### 2. Retrieve Data

#### Fetch All Records
To retrieve all records from the `Add` model:

```python
all_records = Add.objects.all()
```

#### Fetch a Specific Record
To retrieve a single record with a specific ID:

```python
record = Add.objects.get(id=1)
```

#### Filter Records
To filter and update specific records:

```python
Add.objects.filter(id=1).update(num1=10, answer=13)
```

### 3. Update Records

To update fields for specific records:

```python
Add.objects.filter(id=1).update(num1=15, answer=18)
```

### 4. Delete Records

To delete a specific record:

```python
Add.objects.filter(id=1).delete()
```

## Importing Models

To use models in other parts of your Django app, import them as follows:

```python
from .models import Add
```
