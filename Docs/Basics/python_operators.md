# Python Operators

## 1. Arithmetic Operators

- `+` : Addition
- `-` : Subtraction
- `/` : Division
- `*` : Multiplication
- `%` : Modulus
- `**` : Exponentiation
- `//` : Floor Division

**Note**:
- Division `/`  It ensures that the result of the division includes decimal points (i.e., it's a floating-point number), even if the division is between two integers. It also called float division.
- Floor Division `//` rounds down to the nearest integer. Floor division, sometimes also called integer division.
- Modulus `%` returns the remainder of the division of the left operand by the right operand. For example, `7 % 3` returns `1`.
- Exponentiation `**` raises the left operand to the power of the right operand. For example, `2 ** 3` returns `8`.

## 2. Comparison Operators

- `==` : Equal to
- `>` : Greater than
- `<` : Less than
- `>=` : Greater than or equal to
- `<=` : Less than or equal to
- `!=` : Not equal to

## 3. Assignment Operators

- `=` : Assign
- `+=` : Add and assign
- `-=` : Subtract and assign
- `*=` : Multiply and assign
- `/=` : Divide and assign
- `**=` : Exponentiate and assign

**Note**: For example, `a += 2` is equivalent to `a = a + 2`.

## 4. Logical Operators

- `and` : Logical AND
- `or` : Logical OR
- `not` : Logical NOT

**Note**:
- `and` returns `True` if both operands are `True`. For example, `True and False` returns `False`.
- `or` returns `True` if at least one of the operands is `True`. For example, `True or False` returns `True`.
- `not` returns `True` if the operand is `False`, and vice versa. For example, `not True` returns `False`.

## 5. Membership Operators

- `in` : Checks if a value is present in a sequence
- `not in` : Checks if a value is not present in a sequence

**Note**:
- `in` checks for the presence of a value within a sequence (like a list, tuple, or string). For example, `'a' in 'apple'` returns `True`.
- `not in` checks for the absence of a value within a sequence. For example, `'b' not in 'apple'` returns `True`.

## 6. Identity Operators

- `is` : Checks if two variables point to the same object
- `is not` : Checks if two variables point to different objects

**Note**:
- `is` checks for object identity, meaning it returns `True` if both variables point to the same object in memory. For example, `a is b` returns `True` if `a` and `b` are the same object.
- `is not` checks for object non-identity, meaning it returns `True` if both variables do not point to the same object in memory. For example, `a is not b` returns `True` if `a` and `b` are not the same object.

## 7. Bitwise Operators

- `&` : Bitwise AND
- `|` : Bitwise OR
- `~` : Bitwise NOT
- `^` : Bitwise XOR
- `>>` : Bitwise right shift
- `<<` : Bitwise left shift

**Note**: These operators are used to perform bit-level operations on binary numbers. For example, `a & b` performs a bitwise AND operation.

## Reference Code
[View the user inputs code here](../code/python_operators.py)
