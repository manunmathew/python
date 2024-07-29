# Python Loops

Python provides multiple ways to run loops and execute a block of code repeatedly based on a condition or over a sequence. The main types of loops available in Python are the `for` loop and the `while` loop, along with nested loops and loop control statements to manage the flow of loops.

## Types of Loops

### 1. While Loop
The `while` loop repeats a statement or group of statements while a given condition is TRUE. It tests the condition before executing the loop body.

### 2. For Loop
The `for` loop executes a code block multiple times and abbreviates the code that manages the loop variable. It is used for iterating over a sequence (such as a list, tuple, dictionary, set, or string).

### 3. Nested Loops
Nested loops are loops within loops. You can place one loop inside another loop for more complex iteration.

## Loop Control Statements
Loop control statements are used to control loops and change the course of iteration. All the objects produced within the local scope of the loop are deleted when execution is completed.

### 1. Break Statement
The `break` statement terminates the loop's execution and transfers the program's control to the statement next to the loop.

```python
for i in range(10):
    if i == 5:
        break
    print(i)
```
### 2. Continue Statement
The `continue` statement skips the current iteration of the loop. The statements following the `continue` statement are not executed once the Python interpreter reaches the `continue` statement.

```python
for i in range(10):
    if i == 5:
        continue
    print(i)
```

### 3. Pass Statement
The `pass` statement is used when a statement is syntactically necessary, but no code is to be executed.

```python
for i in range(10):
    if i == 5:
        pass
    print(i)
```

## The for Loop
Python's `for` loop is designed to repeatedly execute a code block while iterating through a list, tuple, dictionary, or other iterable objects of Python. The process of traversing a sequence is known as iteration.

### Syntax of the for Loop
```python
sequence = ""
for value in sequence:
#     code block
    pass
```
```python
# Python program to show how the for loop works

# Creating a sequence which is a tuple of numbers
numbers = [4, 2, 6, 7, 3, 5, 8, 10, 6, 1, 9, 2]

# variable to store the square of the number
square = 0

# Creating an empty list
squares = []

# Creating a for loop
for value in numbers:
    square = value ** 2
    squares.append(square)
print("The list of squares is", squares)
```

for value in sequence:
In this case, the variable `value` is used to hold the value of every item present in the sequence before the iteration begins until this particular iteration is completed.

## Using else Statement with for Loop
The `else` statement can be used with a `for` loop. The `else` block is executed when the loop is exhausted.
```python
# Python program to show how to use else statement with for loop

# Creating a sequence
tuple_ = (3, 4, 6, 8, 9, 2, 3, 8, 9, 7)

# Initiating the loop
for value in tuple_:
    if value % 2 != 0:
        print(value)
# giving an else statement
else:
    print("These are the odd numbers present in the tuple")

```
## The range() Function
With the help of the `range()` function, we may produce a series of numbers. `range(10)` will produce values between 0 and 9 (10 numbers).


| Parameter | Description |
|-----------|-------------|
| start     | Optional. An integer number specifying at which position to start. Default is 0 |
| stop      | Required. An integer number specifying at which position to stop (not included). |
| step      | Optional. An integer number specifying the incrementation. Default is 1 |

```python
# Python program to show the working of range() function
print(range(15))
print(list(range(15)))
print(list(range(4, 9)))
print(list(range(5, 25, 4)))
```

## Using range() in a for Loop
To iterate through a sequence of items, we can apply the `range()` method in `for` loops.

## while Loop
While loops are used in Python to iterate until a specified condition is met. However, the statement in the program that follows the `while` loop is executed once the condition changes to false.

### Syntax of the while Loop
```python
while condition:
    # Code block to be executed
    # This code block will execute as long as the condition is true
```
## Using else Statement with while Loop
The `else` statement can be used with the `while` loop. It has the same syntax as used with the `for` loop.

## Single Statement while Block
The loop can be declared in a single statement, similar to the if-else block.

## Detailed Examples of Loop Control Statements


### Continue Statement
The `continue` statement returns the control to the beginning of the loop.

### Break Statement
The `break` statement stops the execution of the loop when the break statement is reached.

### Pass Statement
The `pass` statement is used to create empty loops, classes, functions, and control statements.

***Note***
Loop Control Statements work only inside loop



