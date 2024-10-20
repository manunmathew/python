# Python Functions

## Overview

A function in Python is a block of code that only runs when it is called. Functions are useful for reducing code complexity and repetition.

### Example of a Simple Function

def function_name():
    print("Hello from a function")

In this example, `function_name()` is a function that prints a message when it is called.

## Benefits of Using Functions

- **Reduces Complexity**: Functions allow you to break down your code into smaller, more manageable pieces.
- **Reduces Repetition**: Functions can be reused multiple times throughout your code, reducing the need to write the same code over and over again.

## Variable Classification in Functions

Variables used in functions can be classified into two categories:

### Global Variables

- **Definition**: A global variable is a variable that is declared outside of any function. It can be accessed from anywhere in the program.
- **Example**:

    global_var = "I am global"

    def print_global():
        print(global_var)

    print_global()  # Output: I am global

### Local Variables

- **Definition**: A local variable is a variable that is declared inside a function. It can only be accessed within that function.
- **Example**:

    def print_local():
        local_var = "I am local"
        print(local_var)

    print_local()  # Output: I am local


#### Reference Code



## Arguments
Values can be passed into functions as arguments.

### Positional Arguments
You can specify that a function can have ONLY positional arguments, or ONLY keyword arguments.
```python
def add(a, b):
    print(a + b)

add(1,2)
```


#### Reference Code



### Arbitrary Arguments
    Many arguments that will be passed into your function. add a * before the parameter name in the function definition.
    This way the function will receive a tuple of arguments, and can access the items accordingly:
```python
def num(*a):
    print(a)

num(1,2,3,4,5,a,b)
```
###  Default Arguments Value
If we call the function without argument, it uses the default value

```python
def my_function(country = "Norway"):
  print("I am from " + country)

my_function()
my_function("India")
```

###  Keyword Arguments
You can also send arguments with the key = value syntax.


```python
def add(a, b):
    print(a + b)

add(a=1, b=2) # This way the order of the arguments does not matter.
```
### Arbitrary Keyword Arguments, **kwargs
If you do not know how many keyword arguments that will be passed into your function, add two asterisk: ** before the parameter name in the function definition.

This way the function will receive a dictionary of arguments, and can access the items accordingly:

```python
def person(**data):
    print(data)

person(fname = "Manu ", lname = "Mathew")
```
### Return Values
To let a function return a value, use the return statement
```python
def my_function(x):
  return 5 * x

print(my_function(3))
```
