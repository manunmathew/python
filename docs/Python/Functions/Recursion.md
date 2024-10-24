# Python Function Recursion

## What is Recursion?

Recursion is a fundamental programming concept where a function calls itself in order to solve a problem. This technique is particularly powerful for problems that can be broken down into smaller, similar subproblems. A recursive function typically consists of two main components:

1. **Base Case(s):** The condition(s) under which the function stops calling itself. This prevents infinite recursion and allows the function to return a value.
2. **Recursive Case(s):** The part of the function where it calls itself with a modified argument, gradually moving towards the base case.

Recursion is often used in scenarios where a problem can naturally be divided into similar subproblems, such as:

- Mathematical computations (e.g., calculating factorials, generating Fibonacci sequences)
- Searching and sorting algorithms (e.g., binary search, quicksort)
- Tree and graph traversals
- Dynamic programming problems

## How is Recursion Used in Python?

In Python, recursion is implemented by defining a function that calls itself. The Python interpreter keeps track of these recursive calls using a call stack, which stores information about the function's execution context. Each time a function calls itself, a new frame is added to the call stack. When the base case is reached, the function returns a value, and the stack starts to unwind, returning values up the chain of recursive calls.

Let's now dive into a practical example of recursion by implementing a function to calculate Fibonacci numbers.

## Fibonacci Sequence

The Fibonacci sequence is a series of numbers where each number is the sum of the two preceding ones. It starts with 0 and 1:

\[ 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, \dots \]

## Recursive Function to Print Fibonacci Sequence

The following Python function prints the Fibonacci sequence up to a specified number of terms using recursion:

```python
def print_fibonacci(n, a=0, b=1):
    # Base case: if n is 0, stop the recursion
    if n == 0:
        return
    # Print the current Fibonacci number
    print(a, end=' ')
    # Recursive case: call the function with updated values
    print_fibonacci(n - 1, b, a + b)

# Example usage: print the first 10 Fibonacci numbers
print_fibonacci(10)
```
## How It Works

### Parameters:

- **n**: The number of Fibonacci numbers to print.
- **a**: The current Fibonacci number in the sequence (default is 0).
- **b**: The next Fibonacci number in the sequence (default is 1).

### Base Case:

The recursion stops when `n` reaches 0. This is the base case that prevents the function from calling itself indefinitely.

### Recursive Case:

1. The function prints the current Fibonacci number (`a`).
2. It then calls itself recursively, reducing `n` by 1, setting `b` as the new `a`, and `a + b` as the new `b`.

## Example Execution

If you run the function with `print_fibonacci(10)`, the output will be:  0 1 1 2 3 5 8 13 21 34


### Explanation of Execution:

1. The function begins with the initial values `a = 0` and `b = 1`.
2. It prints `a`, which is the first Fibonacci number.
3. The function then recursively calls itself with updated parameters: `n-1`, `b` as the new `a`, and `a + b` as the new `b`.
4. This continues until `n` reaches 0, which is when the recursion stops.

