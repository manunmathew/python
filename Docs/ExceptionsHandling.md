# Exceptions Handling

Exceptions : Exceptions are un wanted errors that occurs during the run time of a program
if you have some suspicious code that may raise an exception you can defend your program by placing the suspicious code in try and except block to handle the error


## Runtime exceptions
    by end user
    ValueError, IndexError
## Logic exception
    SyntaxError, IndentationError


### Common exceptions

    AttributeError : Raised when attribute reference or assignment fails
    ImportError : Raised when an imported module does not exist
    KeyError:	Raised when a key does not exist in a dictionary
    NameError:	Raised when a variable does not exist
    ZeroDivisionError:	Raised when the second operator in a division is zero
    ValueError:	Raised when there is a wrong value in a specified data type
    TypeError:	Raised when two different types are combined
    FileNotFoundError: Raises, when a file is not found

```python
try:
  print(x) # code to be executed
except:
  print("An exception occurred") # code executes when an error
```



































