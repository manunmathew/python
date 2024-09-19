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


