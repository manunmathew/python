# Assertion Exception Handling

In Python, assertions are a debugging tool to test assumptions made in the code. When an `assert` statement fails, an `AssertionError` is raised.

## Syntax:
```python
assert condition, "Optional error message"
```

## Example
```python
def validate_age(age):
    assert age >= 18, "Age must be at least 18"
    return age

try:
    validate_age(16)
except AssertionError as e:
    print(e)

Output: Age must be at least 18
```

# Raise keyword Exception Handling
Python raise Keyword is used to raise exceptions or errors. to manually trigger an exception

```python
try:
	num = int(input("Enter a number"))
    if num >= 1 and num <= 10 :
        print("Success")
    else:
        raise Exeption:

except Exeption:
	print("Please input a number between 1 and 10")

```
