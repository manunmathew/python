# Conditional Statements

Conditional statements control the flow of a program by executing certain pieces of code only when specific conditions are met. Here, we discuss three main types of conditional statements in programming: `if`, `else`, and `elif`.

## If Statement

The `if` statement is a control flow statement that allows code to run only when a particular condition is satisfied.

### Syntax

```python
if (condition):
    # body of if

```
### Example
```python
age = 18
if age >= 18:
    print("You are eligible to vote.")
```
In this example, the message "You are eligible to vote." will be printed only if the condition age >= 18 is true.

### Reference Code
[View the user inputs code here](../code/ConditionalStatements/if.py)


## Else Statement
The else statement follows an if statement and runs a block of code if the if condition is false.

### Syntax
```python
if (condition):
    # body of if
else:
    # body of else
```
### Example
```python
age = 16
if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")
In this example, the message "You are not eligible to vote." will be printed because the condition age >= 18 is false.
```
***Note***
No condition is required for the else statement. It acts as a catch-all for any scenario where the if condition is not met.

### Reference Code


## Elif Statement
The elif statement allows you to check multiple conditions. It stands for "else if" and is used when you want to test more than two conditions.

### Syntax
```python
if (condition):
    # body of if
elif (condition):
    # body of elif
elif (condition):
    # body of elif
...
else:
    # body of else
```
### Example
```python
score = 75
if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
else:
    print("Grade: D")
```
In this example, the message "Grade: C" will be printed because the score of 75 meets the condition score >= 70.

***Note***
Just like with else, no condition is required for the final else block. It will execute if none of the preceding if or elif conditions are met.

### Reference Code



### Complete Example
Here's a complete example demonstrating the use of if, else, and elif statements in a single block of code:
```python
age = 20
score = 85

# Checking voting eligibility
if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")

# Checking grade based on score
if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
else:
    print("Grade: D")
```
This example first checks if a person is eligible to vote based on their age, and then it checks the grade based on their score. It demonstrates how to use if, else, and elif statements effectively to control the flow of a program.
