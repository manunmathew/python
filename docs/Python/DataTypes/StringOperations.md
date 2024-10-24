# String Operations in Python

## Checking Data Type

### `type()` function

- **Purpose**: Returns the data type of an object.
  - Example:
    - `y = 5`
      - `print(type(y))` returns `<class 'int'>`
    - `z = "hello"`
      - `print(type(z))` returns `<class 'str'>`
- This is useful to confirm the type of a variable or expression, especially when debugging or when working with dynamic or user-generated data.

## Indexing

- Index starts from 0 and includes white spaces.

`x = "example string"`

- `print(x[0])` prints the first character: 'e'
- `print(x[0:15])` prints characters from index 0 to 14: 'example string'
- `print(x[-1])` prints the last character using negative indexing: 'g'

## String Methods

### Case Conversion

- **Convert to upper case**
  - `print(x.upper())` converts all characters to upper case: 'EXAMPLE STRING'
- **Convert to lower case**
  - `print(x.lower())` converts all characters to lower case: 'example string'
- **Convert to title case**
  - `print(x.title())` converts the first character of each word to upper case: 'Example String'
- **Swap case**
  - `print(x.swapcase())` swaps the case of all characters: 'EXAMPLE STRING'
- **Capitalize**
  - `print(x.capitalize())` converts the first character to upper case and the rest to lower case: 'Example string'

### Boolean Checks

- **Check if all characters are upper case**
  - `print(x.isupper())` returns `True` if all characters are upper case, otherwise `False`
- **Check if all characters are lower case**
  - `print(x.islower())` returns `True` if all characters are lower case, otherwise `False`
- **Check if all characters are alphabetic**
  - `print(x.isalpha())` returns `True` if all characters are alphabetic, otherwise `False`
- **Check if all characters are numeric**
  - `print(x.isnumeric())` returns `True` if all characters are numeric, otherwise `False`
- **Check if all characters are alphanumeric**
  - `print(x.isalnum())` returns `True` if all characters are alphanumeric (letters and numbers), otherwise `False`

## Finding Substrings

### `find` method

- **Purpose**: Returns the index of the first occurrence of the substring. Returns -1 if the substring is not found.
  - Example:
    - `print(x.find("to"))` returns index of 'to' if found
    - `print(x.find("hello"))` returns -1 if 'hello' is not found

### `index` method

- **Purpose**: Returns the index of the first occurrence of the substring. Raises a `ValueError` if the substring is not found.
  - Example:
    - `print(x.index("to"))` returns index of 'to' if found
    - `print(x.index("hello"))` raises ValueError if 'hello' is not found

### `rfind` method

- **Purpose**: Returns the index of the last occurrence of the substring. Returns -1 if the substring is not found.
  - Example:
    - `print(x.rfind("to"))` returns last index of 'to' if found
    - `print(x.rfind("hello"))` returns -1 if 'hello' is not found

### `count` method

- **Purpose**: Returns the number of occurrences of the substring in the string.
  - Example:
    - `print(x.count("to"))` returns the number of times 'to' appears in the string



## String Concatenation in Python

In Python, there are multiple ways to concatenate, or combine, strings. Here are some common methods:

### Using the `+` Operator

You can concatenate two strings using the `+` operator. This is the most straightforward method.
```python
a = "Hello"
b = "World"
c = a + b
print(c)  # Output: HelloWorld
```
### Using the `join()` Method

The `join()` method takes all items in an iterable and joins them into one string. A string must be specified as the separator.

```python
myDict = {"name": "John", "country": "Norway"}
mySeparator = " "

x = mySeparator.join(myDict)
print(x)  # Output: name country
```
Note: When using a dictionary, the `join()` method joins the keys, not the values.

### Using the `%` Operator

You can use the `%` operator to concatenate strings. This method is similar to C-style string formatting.
```python
a = "Hello"
b = "World"
print("%s%s" % (a, b))  # Output: HelloWorld
```
### Using the `format()` Method

The `format()` method formats the specified value(s) and inserts them inside the string's placeholder. The placeholder is defined using curly brackets `{}`.
```python
a = "Hello"
b = "World"
print("{}{}".format(a, b))  # Output: HelloWorld
```

- **`+` Operator**: Simple and straightforward.
- **`join()` Method**: Useful for joining an iterable with a specified separator.
- **`%` Operator**: Similar to C-style string formatting.
- **`format()` Method**: Flexible and allows for more complex formatting.

### Using the `replace()` Method

The `replace()` method replaces a specified phrase with another specified phrase.

    string.replace(oldvalue, newvalue, count)

- **Parameter Description**
  - `oldvalue`: Required. The string to search for.
  - `newvalue`: Required. The string to replace the old value with.
  - `count`: Optional. A number specifying how many occurrences of the old value you want to replace. Default is all occurrences.

### `strip()` Method

The `strip()` method removes any leading and trailing whitespaces.

    txt = "     banana     "
    x = txt.strip()
    print(x)

Output:

    banana

- **`lstrip()`**: Returns a left-trimmed version of the string.
- **`rstrip()`**: Returns a right-trimmed version of the string.

## Slicing

You can return a range of characters by using the slice syntax.

Specify the start index and the end index, separated by a colon, to return a part of the string.

Get the characters from position 2 to position 5 (not included):

    b = "Hello, World!"
    print(b[2:5])

### Slice From the Start

By leaving out the start index, the range will start at the first character. Get the characters from the start to position 5 (not included):

    b = "Hello, World!"
    print(b[:5])

### Slice To the End

By leaving out the end index, the range will go to the end. Get the characters from position 2, and all the way to the end:

    b = "Hello, World!"
    print(b[2:])

### Negative Indexing

Use negative indexes to start the slice from the end of the string. From: "o" in "World!" (position -5) To, but not included: "d" in "World!" (position -2):

    b = "Hello, World!"
    print(b[-5:-2])

### Reverse

Reverse the string:

    s = "Hello, World!"
    print(s[::-1])

### Even Position

To get characters at even positions in the string:

    s = "Hello, World!"
    print(s[::2])

## Reference Code

