# Python String Formatting Guide

## Common Formatting Types

### Fixed-point number
- **`f`**: Fixed-point number. Displays the number as a float.

  Example:
  value = 123.456
  print(f"{value:.2f}")  # Output: 123.46

### General format
- **`g`**: General format. Uses either fixed-point or scientific notation, depending on the value and the precision.

  Example:
  value = 1234567.89
  print(f"{value:.2g}")  # Output: 1.2e+06

### Exponential notation
- **`e`**: Exponential notation. Displays the number in scientific notation.

  Example:
  value = 1234.5678
  print(f"{value:.2e}")  # Output: 1.23e+03

### Percentage
- **`%`**: Percentage. Multiplies the number by 100 and displays it with a percent sign.

  Example:
  value = 0.1234
  print(f"{value:.2%}")  # Output: 12.34%

### String
- **`s`**: String format.

  Example:
  value = "Hello"
  print(f"{value:s}")  # Output: Hello

### Integer
- **`d`**: Decimal integer.

  Example:
  value = 123
  print(f"{value:d}")  # Output: 123

### Binary
- **`b`**: Binary format.

  Example:
  value = 123
  print(f"{value:b}")  # Output: 1111011

### Octal
- **`o`**: Octal format.

  Example:
  value = 123
  print(f"{value:o}")  # Output: 173

### Hexadecimal
- **`x`**: Hexadecimal format (lowercase).

  Example:
  value = 123
  print(f"{value:x}")  # Output: 7b

- **`X`**: Hexadecimal format (uppercase).

  Example:
  value = 123
  print(f"{value:X}")  # Output: 7B

## Alignment and Width

### Left align
  Example:
  value = 123
  print(f"{value:<10}")  # Output: '123       '

### Right align
  Example:
  value = 123
  print(f"{value:>10}")  # Output: '       123'

### Center align
  Example:
  value = 123
  print(f"{value:^10}")  # Output: '   123    '

### Zero padding
  Example:
  value = 123
  print(f"{value:010}")  # Output: '0000000123'

## Combining Width and Precision

You can combine width and precision for floating-point numbers:

  Example:
  value = 123.456
  print(f"{value:10.2f}")  # Output: '    123.46'
