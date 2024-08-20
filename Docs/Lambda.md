# Lambda Functions in Python

## Overview

Lambda functions in Python are a way to create small, anonymous functions without having to define them using the standard `def` keyword. These functions are typically used for short periods of time and can be particularly useful when you need a simple function for a specific operation.

### Characteristics of Lambda Functions

- **Single Line Function**: Lambda functions are defined in a single line.
- **Multiple Arguments**: They can take any number of arguments.
- **Single Expression**: Lambda functions can only have one expression, which is evaluated and returned.
- **Anonymous**: Lambda functions are anonymous, meaning they do not have a name unless assigned to a variable.

### Syntax

The basic syntax for creating a lambda function is as follows:

```python
lambda arguments : expression
```

### Example

Here’s a simple example of a lambda function that adds 10 to a given number:

```python
add_ten = lambda x: x + 10
print(add_ten(5))  # Output: 15
```

## Built-in Functions with Lambda

Lambda functions are often used with Python’s built-in functions such as `filter()`, `map()`, and `reduce()`.

### 1. `filter()`

The `filter()` function constructs an iterator from elements of an iterable for which a function returns true. A lambda function can be passed as the function argument to filter elements.

**Example**:

```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  # Output: [2, 4, 6, 8]
```

### 2. `map()`

The `map()` function applies a given function to all the items in an input list. You can use a lambda function to define the operation to be applied to each item.

**Example**:

```python
numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x**2, numbers))
print(squared_numbers)  # Output: [1, 4, 9, 16, 25]
```

### 3. `reduce()`

The `reduce()` function is used to apply a particular function passed in its argument to all of the list elements. It’s part of the `functools` module.

**Example**:

```python
from functools import reduce

numbers = [1, 2, 3, 4, 5]
sum_of_numbers = reduce(lambda x, y: x + y, numbers)
print(sum_of_numbers)  # Output: 15
```
