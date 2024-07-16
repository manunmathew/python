## Python String Formatting

### 1. F-String (Formatted String Literals)
Introduced in Python 3.6, f-strings offer a way to embed expressions inside string literals using curly braces `{}`.

**Example:**
```python
name = input("Company Name: ")
location = input("Company location: ")
print(f"{name} located in {location}")
```
### 2. `%s, %d, %f` (Old-style String Formatting)
These specifiers are used with the `%` operator to format strings. `%s` is used for strings, `%d` for integers, and `%f` for floating-point numbers.

**Example:**
```python
name = "OpenAI"
age = 10
height = 5.95
print("Name: %s, Age: %d, Height: %.2f" % (name, age, height))
```
