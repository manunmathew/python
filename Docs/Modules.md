# Modules in Python

In Python, a **module** is a collection of functions, classes, and variables that are bundled together to provide specific functionalities. Modules allow you to organize your code into separate files and reuse functions across multiple scripts. Python comes with a large standard library of built-in modules, which provide a wide range of utilities, from mathematical operations to system-level interactions.

## Built-in Modules

Python's standard library includes many built-in modules that you can use without the need for external installation. Below are some of the most commonly used built-in modules:

### 1. math
The `math` module provides access to mathematical functions like trigonometry, logarithms, and more. It is particularly useful for performing precise mathematical operations.

**Common Functions:**
- `math.sqrt(x)`: Returns the square root of `x`.
- `math.sin(x)`: Returns the sine of `x` (in radians).
- `math.cos(x)`: Returns the cosine of `x` (in radians).
- `math.factorial(x)`: Returns the factorial of `x`.
- `math.pi`: Returns the value of π (pi).

**Example:**
- `math.sqrt(16)` returns `4.0`
- `math.pi` returns `3.141592653589793`

### 2. time
The `time` module provides various functions to manipulate time and perform time-related tasks, such as sleeping for a set amount of time, measuring the performance of code, or retrieving the current time.

**Common Functions:**
- `time.sleep(seconds)`: Suspends execution for the given number of seconds.
- `time.time()`: Returns the current time in seconds since the epoch.
- `time.ctime()`: Converts a time expressed in seconds since the epoch to a string representing local time.

**Example:**
- `time.sleep(2)` pauses the program for 2 seconds.
- `time.time()` returns the current time in seconds since the epoch.

### 3. datetime
The `datetime` module provides classes for manipulating dates and times. It includes the ability to perform arithmetic operations on dates and times, as well as formatting and parsing date strings.

**Common Classes and Methods:**
- `datetime.datetime.now()`: Returns the current date and time.
- `datetime.date.today()`: Returns the current date.
- `datetime.timedelta`: Represents the difference between two dates or times.
- `datetime.datetime.strftime(format)`: Formats a datetime object as a string.

**Example:**
- `datetime.datetime.now()` returns the current date and time.
- `datetime.date.today()` returns the current date.

### 4. calendar
The `calendar` module allows you to output calendars and provides functions to manipulate dates. You can use it to display calendars, check if a year is a leap year, and more.

**Common Functions:**
- `calendar.month(year, month)`: Returns a string representing the calendar for a specific month.
- `calendar.isleap(year)`: Returns `True` if the year is a leap year, otherwise `False`.
- `calendar.weekday(year, month, day)`: Returns the day of the week for a given date.

**Example:**
- `calendar.month(2024, 8)` displays the calendar for August 2024.
- `calendar.isleap(2024)` returns `True`, because 2024 is a leap year.

### 5. random
The `random` module provides functions to generate random numbers, select random items from sequences, shuffle sequences, and more. It is commonly used in simulations, games, and testing.

**Common Functions:**
- `random.random()`: Returns a random float number between 0.0 and 1.0.
- `random.randint(a, b)`: Returns a random integer between `a` and `b`.
- `random.choice(sequence)`: Returns a random element from a non-empty sequence.
- `random.shuffle(sequence)`: Shuffles the sequence in place.

**Example:**
- `random.randint(1, 10)` returns a random integer between 1 and 10.
- `random.shuffle(my_list)` shuffles the list in place.

### 6. os
The `os` module provides a way to interact with the operating system. It allows you to perform tasks such as creating, removing, and renaming files or directories, as well as retrieving environmental variables.

**Common Functions:**
- `os.getcwd()`: Returns the current working directory.
- `os.listdir(path)`: Returns a list of entries in the directory given by path.
- `os.mkdir(path)`: Creates a directory named `path`.
- `os.remove(path)`: Removes the file `path`.
- `os.rmdir(path)`: Removes the directory `path`.

**Example:**
- `os.getcwd()` returns the current working directory.
- `os.mkdir('new_folder')` creates a new directory named "new_folder".

---

This document provides an overview of some of the most commonly used built-in modules in Python. Each module offers a wide array of functions and capabilities that help make Python a versatile and powerful programming language.
