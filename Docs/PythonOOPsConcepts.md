# Object-Oriented Programming
oops concepts in Python is to bind the data and the functions that work together as a single unit so that no other part of the code can access this data.
## Python Class
A class is a collection of objects. A class contains the blueprints or the prototype from which the objects are being created.

Function that defined inside class is known as member function or methods

Class Definition Syntax:

class ClassName:
   # Statement-1
   .
   .
   .
   # Statement-N

## Python Objects

## self in Python class

In object oriented programming self is reference to the current instance of the class. it is used to access variables and methods that belongs to the class. it allows the methods to access attributes and other methods on the same object

## Static (Class) Variables:
 A static variable is a variable that is shared among all instances of a class. It is defined within the class but outside any methods.

## Dynamic (Instance) Variables:
A dynamic variable is a variable that is unique to each instance of a class. It is usually defined within methods,

## constructor in oops
A constructor is a special type of method that is automatically called when an instance of a class is created. The main purpose of a constructor is to initialize the values of an object's attributes directly within the class.
```python
class maths:
    def __init__(self, a, b):
        print(a+b)

obj = maths(1,2)
```
## inheritance

inheritance that allows to define a class that inherit all the methods and properties from another class

inheritance are classified into 5 type
   1) Single Inheritance
   2) Multiple Inheritance
   3) Multilevel Inheritance
   4) Hierarchical Inheritance
   5) Hybrid Inheritance

### 1. Single Inheritance
In single inheritance, a child class inherits from only one parent class. This is the most basic form of inheritance.

```python
class Parent:
    def parent_method(self):
        print("This is the parent method.")

class Child(Parent):
    def child_method(self):
        print("This is the child method.")
```
### 2. Multiple Inheritance
In multiple inheritance, a child class inherits from more than one parent class, allowing it to access properties and methods of all its parent classes.

```python
class Parent1:
    def method1(self):
        print("This is method1 from Parent1.")

class Parent2:
    def method2(self):
        print("This is method2 from Parent2.")

class Child(Parent1, Parent2):
    def child_method(self):
        print("This is the child method.")
```
### 3. Multilevel Inheritance
In multilevel inheritance, a class inherits from a parent class, which itself is a child of another class, forming a chain of inheritance.

```python
class Grandparent:
    def grandparent_method(self):
        print("This is the grandparent method.")

class Parent(Grandparent):
    def parent_method(self):
        print("This is the parent method.")

class Child(Parent):
    def child_method(self):
        print("This is the child method.")
```
### 4. Hierarchical Inheritance
In hierarchical inheritance, multiple child classes inherit from a single parent class, allowing multiple classes to reuse the code of a common parent class.


```python
class Parent:
    def parent_method(self):
        print("This is the parent method.")

class Child1(Parent):
    def child1_method(self):
        print("This is the child1 method.")

class Child2(Parent):
    def child2_method(self):
        print("This is the child2 method.")
```
### 5. Hybrid Inheritance
Hybrid inheritance is a combination of two or more types of inheritance. It involves multiple, hierarchical, or multilevel inheritance patterns to create a complex inheritance structure.

```python
class Grandparent:
    def grandparent_method(self):
        print("This is the grandparent method.")

class Parent1(Grandparent):
    def parent1_method(self):
        print("This is the parent1 method.")

class Parent2(Grandparent):
    def parent2_method(self):
        print("This is the parent2 method.")

class Child(Parent1, Parent2):
    def child_method(self):
        print("This is the child method.")
```
