# Python File Handling

File handling is an essential part of many Python programs. It allows programs to read, write, and manipulate files. Python provides built-in functions and methods to handle files effectively.

## 1. Opening a File

Python uses the `open()` function to open files. This function returns a file object, which provides methods for interacting with the file.

### Syntax:
```python
    file_object = open(file_name, mode)
```
### Parameters:
- `file_name`: Name of the file to be opened (can include the path).
- `mode`: The mode in which the file is opened, such as read, write, append, etc.

### Common Modes:
- `'r'`: Read (default) – Opens a file for reading, errors if the file does not exist.
- `'w'`: Write – Opens a file for writing, creates the file if it doesn’t exist, and truncates if it does.
- `'a'`: Append – Opens a file for appending, creates the file if it doesn’t exist.
- `'b'`: Binary – Binary mode for non-text files (e.g., images or executables).
- `'t'`: Text (default) – Text mode for working with textual files.

### Example:
```python
    file = open("example.txt", "r")
```
## 2. Reading from a File

Once a file is opened in reading mode, several methods are available to read the file's content.

### Common Methods:
- `read(size)`: Reads `size` number of characters from the file. If `size` is omitted, it reads the whole file.
- `readline()`: Reads one line from the file.
- `readlines()`: Reads all lines and returns them as a list.

### Example:
```python
    # Reading entire content
    file = open("example.txt", "r")
    content = file.read()
    print(content)

    # Reading line by line
    file = open("example.txt", "r")
    for line in file:
        print(line)
    file.close()
```
## 3. Writing to a File

When opening a file in writing mode (`'w'`) or appending mode (`'a'`), Python allows data to be written to the file.

### Common Methods:
- `write(string)`: Writes a string to the file.
- `writelines(list)`: Writes a list of strings to the file.

### Example:
```python
    # Writing to a file
    file = open("example.txt", "w")
    file.write("Hello, World!")
    file.close()

    # Appending to a file
    file = open("example.txt", "a")
    file.write("\nThis is appended.")
    file.close()
```
## 4. Closing a File

After working with a file, it is important to close it using the `close()` method to free up system resources.

### Example:
```python
    file = open("example.txt", "r")
    content = file.read()
    file.close()
```
## 5. Using `with` for File Handling

Using `with` is a more Pythonic and safer way to work with files. It automatically closes the file after the block of code is executed, even if an exception is raised.

### Example:
```python
    with open("example.txt", "r") as file:
        content = file.read()
        print(content)
    # File is automatically closed after the block
```
## 6. File Modes in Detail

| Mode | Description |
|------|-------------|
| `'r'` | Read mode, file must exist. |
| `'w'` | Write mode, creates or truncates the file. |
| `'a'` | Append mode, creates if file doesn’t exist. |
| `'r+'` | Read and write mode, file must exist. |
| `'w+'` | Write and read mode, creates or truncates the file. |
| `'a+'` | Append and read mode, creates if file doesn’t exist. |
| `'rb'`, `'wb'`, `'ab'` | Same as above, but in binary mode. |

## 7. Handling Exceptions

Python provides a `try-except` block to handle potential file handling errors, such as the file not existing.

### Example:
```python
    try:
        file = open("nonexistent.txt", "r")
    except FileNotFoundError:
        print("The file does not exist.")
```
## 8. Working with Binary Files

To handle non-text files like images or executables, open the file in binary mode (`'b'`).

### Example:
```python
    with open("image.png", "rb") as file:
        data = file.read()
```
## 9. File Object Methods

A file object has various useful methods:
- `seek(offset, from_what)`: Moves the file pointer to a specific location.
- `tell()`: Returns the current position of the file pointer.
- `truncate(size)`: Truncates the file to the given size.

### Example:
```python
    file = open("example.txt", "r")
    file.seek(10)  # Move to the 10th byte
    position = file.tell()  # Get current pointer position
    file.close()
```
## 10. Checking if File Exists

You can check if a file exists using the `os` module or the `pathlib` module.

### Example using `os`:
```python
    import os
    if os.path.exists("example.txt"):
        print("File exists")
```
### Example using `pathlib`:
```python
    from pathlib import Path
    file = Path("example.txt")
    if file.exists():
        print("File exists")
```
