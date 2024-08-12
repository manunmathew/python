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


## Reference Code
[View the code here](../code/Functions/basic.py)


## Arguments
Values can be passed into functions as arguments.

### Positional Arguments
You can specify that a function can have ONLY positional arguments, or ONLY keyword arguments.
```python
def add(a, b):
    print(a + b)

add(a = 1, b = 2)
```


## Reference Code
[View the code here](../code/Functions/arguments.py)
